from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"  # Points to the .env file

# Create an instance of Settings
settings = Settings()

