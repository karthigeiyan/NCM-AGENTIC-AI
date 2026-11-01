import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME", "Adaptive NCM Enterprise")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://ncm_user:ncm_password@localhost:5432/ncm_db")
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

settings = Settings()
