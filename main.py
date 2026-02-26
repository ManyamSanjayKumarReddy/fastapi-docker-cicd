from fastapi import FastAPI
from typing import Dict

app = FastAPI(title="My FastAPI Server")

@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Welcome to FastAPI Server with CI/CD pipeline!"}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "fastapi-server",
        "version": "1.0.0"
    }

@app.get("/data")
def get_data() -> Dict[str, str]:
    """Data endpoint"""
    return {
        "message": "Hello this is from server endpoint",
        "server": "FastAPI",
        "endpoint": "/data",
        "version": "2.0 & cicd pipeline is working fine"
    }