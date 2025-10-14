"""
Budgeting advice endpoint.
Accepts a free-form question and returns budgeting advice from the LLM.
"""

import logging
import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from llm_service.utils import get_advice_prompt


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

# Ollama API configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:1.7b"


class AdviceRequest(BaseModel):
    """Request body for budgeting advice.
    
    Example:
    {
        "question": "How can I reduce my monthly grocery expenses?"
    }
    """
    question: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="User's budgeting question"
    )


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
        
        logger.info(f"Processing advice request: {question[:50]}...")
        
        # Generate prompt
        prompt = get_advice_prompt(question)
        logger.debug(f"Prompt: {prompt[:100]}...")
        
        # Call Ollama API
        ollama_request = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 150  # Limit response length for faster responses
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
        advice_text = ollama_data.get("response", "").strip()
        if not advice_text:
            advice_text = ollama_data.get("thinking", "").strip()
        
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

