"""
Expense summarization endpoint.
Accepts a list of expenses and returns a natural-language summary from the LLM.
"""

import logging
import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from llm_service.utils import get_summarize_prompt


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

# Ollama API configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:1.7b"


class ExpenseItem(BaseModel):
    """Single expense entry."""
    category: str = Field(..., description="Expense category (e.g., 'Food', 'Transport')")
    amount: float = Field(..., gt=0, description="Expense amount in dollars")


class ExpenseRequest(BaseModel):
    """Request body for expense summarization.
    
    Example:
    {
        "expenses": [
            {"category": "Food", "amount": 45.50},
            {"category": "Transport", "amount": 20.00},
            {"category": "Entertainment", "amount": 35.00}
        ]
    }
    """
    expenses: List[ExpenseItem] = Field(..., min_items=1, description="List of expense items")


class SummaryResponse(BaseModel):
    """Response containing the expense summary."""
    summary: str = Field(..., description="Natural language summary of expenses")
    total_amount: float = Field(..., description="Total amount of all expenses")
    expense_count: int = Field(..., description="Number of expense items")


@router.post("/api/summarize", response_model=SummaryResponse, tags=["Expenses"])
async def summarize_expenses(request: ExpenseRequest):
    """
    Summarize expense data using the local Ollama LLM.
    
    This endpoint accepts a list of expenses and returns a natural-language
    summary with spending insights from the Qwen3:8b model.
    
    Args:
        request: ExpenseRequest containing list of expenses
        
    Returns:
        SummaryResponse with summary text and totals
        
    Raises:
        HTTPException: If Ollama service is unavailable or request fails
    """
    try:
        # Convert Pydantic models to dictionaries
        expenses = [exp.dict() for exp in request.expenses]
        
        # Calculate totals
        total = sum(exp['amount'] for exp in expenses)
        count = len(expenses)
        
        # Generate prompt
        prompt = get_summarize_prompt(expenses)
        
        logger.info(f"Summarizing {count} expenses totaling ${total:.2f}")
        logger.debug(f"Prompt: {prompt[:100]}...")
        
        # Call Ollama API
        ollama_request = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 200  # Limit response length for faster responses
            }
        }
        
        response = requests.post(
            OLLAMA_URL,
            json=ollama_request,
            timeout=120
        )
        response.raise_for_status()
        
        # Extract response text
        ollama_data = response.json()
        # Try response field first, then thinking field (for reasoning models)
        summary_text = ollama_data.get("response", "").strip()
        if not summary_text:
            summary_text = ollama_data.get("thinking", "").strip()
        
        if not summary_text:
            raise ValueError("Empty response from Ollama")
        
        logger.info(f"Successfully generated summary: {summary_text[:50]}...")
        
        return SummaryResponse(
            summary=summary_text,
            total_amount=total,
            expense_count=count
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
        logger.error(f"Unexpected error during summarization: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )

