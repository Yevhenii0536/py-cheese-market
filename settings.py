from pydantic.v1 import BaseSettings
from dotenv import load_dotenv

import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


class Settings(BaseSettings):
    PROJECT_NAME: str = "Cheeese market"

    DATABASE_URL: str = DATABASE_URL or ""

    class Config:
        case_sensitive = True
        env_file = ".env"



settings = Settings()