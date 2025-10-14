"""
LLM Microservice - Main Application
====================================

A FastAPI microservice that interacts with a locally running Ollama model (Qwen3:8b)
to analyze and summarize expense data for a budget tracker app.

Features:
- Expense summarization with natural language insights
- Budgeting advice based on user questions
- Clean JSON API responses
- Error handling and logging

Run with:
    uvicorn main:app --reload --port 8000
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import summarize, advice


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI application
app = FastAPI(
    title="LLM Budget Advisor",
    description="A microservice for expense analysis and budgeting advice using local Ollama LLM",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(summarize.router)
app.include_router(advice.router)


@app.get("/", tags=["Health"])
async def root():
    """
    Root endpoint - Health check and API information.
    
    Returns:
        Basic API information and status
    """
    return {
        "service": "LLM Budget Advisor",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "summarize": "/api/summarize",
            "advice": "/api/advice",
            "docs": "/docs"
        }
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint.
    
    Returns:
        Service health status
    """
    return {
        "status": "healthy",
        "service": "llm_service"
    }


if __name__ == "__main__":
    import uvicorn
    
    logger.info("Starting LLM Budget Advisor service...")
    logger.info("Ollama should be running on http://localhost:11434")
    logger.info("Model: qwen2.5:3b")
    
    # Run the application
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


