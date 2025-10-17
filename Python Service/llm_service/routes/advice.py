import logging
import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from llm_service.utils import get_advice_prompt


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:1.7b"


class ExpenseItem(BaseModel):
    """Single expense entry."""
    category: str = Field(..., description="Expense category (e.g., 'Food', 'Transport')")
    amount: float = Field(..., gt=0, description="Expense amount in dollars")


class AdviceRequest(BaseModel):
    """Request body for budgeting advice.
    
    Example:
    {
        "question": "How can I reduce my monthly grocery expenses?",
        "expenses": [
            {"category": "Food", "amount": 300.50},
            {"category": "Transport", "amount": 150.00}
        ],
        "budget": 500.00
    }
    """
    question: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="User's budgeting question"
    )
    expenses: List[ExpenseItem] = Field(..., min_items=1, description="List of expense items")
    budget: float = Field(..., gt=0, description="User's budget amount in dollars")



class AdviceResponse(BaseModel):
    """Response containing budgeting advice."""
    advice: str = Field(..., description="Budgeting advice from the LLM")
    question: str = Field(..., description="Original question asked")


@router.post("/api/advice", response_model=AdviceResponse, tags=["Advice"])
async def get_budgeting_advice(request: AdviceRequest):
    """
    Get budgeting advice from the local Ollama LLM.
    
    This endpoint accepts a free-form question about budgeting and returns
    a concise, practical tip from the Qwen3:8b model.
    
    Args:
        request: AdviceRequest containing the user's question
        
    Returns:
        AdviceResponse with advice text
        
    Raises:
        HTTPException: If Ollama service is unavailable or request fails
    """
    try:
        question = request.question.strip()
        expenses = [exp.dict() for exp in request.expenses]
        budget = request.budget
        
        # Calculate totals for logging
        total = sum(exp['amount'] for exp in expenses)
        count = len(expenses)
        budget_status = "over" if total > budget else "under" if total < budget else "at"
        
        logger.info(f"Processing advice request: {question[:50]}... with {count} expenses totaling ${total:.2f} ({budget_status} budget of ${budget:.2f})")

        prompt = get_advice_prompt(question, expenses, budget)
        logger.debug(f"Prompt: {prompt[:100]}...")
        
        ollama_request = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.6,
                "num_predict": 500
            }
        }
        
        response = requests.post(
            OLLAMA_URL,
            json=ollama_request,
            timeout=120
        )
        response.raise_for_status()
        
        ollama_data = response.json()

        advice_text = ollama_data.get("response", "").strip()
        if not advice_text:
            advice_text = ollama_data.get("response", "").strip()
        
        if not advice_text:
            raise ValueError("Empty response from Ollama")
        
        logger.info(f"Successfully generated advice: {advice_text[:50]}...")
        
        return AdviceResponse(
            advice=advice_text,
            question=question
        )
        
    except requests.exceptions.ConnectionError:
        logger.error("Failed to connect to Ollama service")
        raise HTTPException(
            status_code=503,
            detail="Unable to connect to Ollama service. Please ensure Ollama is running on http://localhost:11434"
        )
    except requests.exceptions.Timeout:
        logger.error("Ollama request timed out")
        raise HTTPException(
            status_code=504,
            detail="Request to Ollama timed out. Please try again."
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"Ollama request failed: {str(e)}")
        raise HTTPException(
            status_code=502,
            detail=f"Failed to communicate with Ollama: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error during advice generation: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )

