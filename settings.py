from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Cheeese market"

    DATABASE_URL: str = ""

    class Config:
        case_sensitive = True
        env_file = ".env"



settings = Settings()