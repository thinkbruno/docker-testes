import os


class Config:
    DEBUG = os.getenv("DEBUG", "True") == "True"
    DATABASE_URL = os.getenv("DATABASE_URL")
