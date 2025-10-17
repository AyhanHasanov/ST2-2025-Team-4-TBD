import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from llm_service.routes import summarize, advice


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="LLM Budget Advisor",
    description="A microservice for expense analysis and budgeting advice using local Ollama LLM",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    logger.info("Model: qwen1.7:3b")
    
    # Run the application
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


