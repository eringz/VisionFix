# # from pydantic import BaseSettings # this is the depreciated libs.do
# from pydantic_settings import BaseSettings
# from typing import ClassVar

# class Settings(BaseSettings):
#     DATABASE_URL = ClassVar[str]

#     class Config:
#         env_file = ".env"

# settings = Settings()
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        # env_file = ".env"  # Points to the .env file
        # env_file = "VissionFix/backend/.env"
        env_file = os.path.join(os.path.dirname(__file__), '.env') 

# Create an instance of Settings
settings = Settings()

# from pydantic_settings import BaseSettings
# from typing import ClassVar

# class Settings(BaseSettings):
#     DATABASE_URL: ClassVar[str]  # Properly declare DATABASE_URL as a ClassVar

#     class Config:
#         env_file = ".env"  # Specify the environment file for configuration

# settings = Settings()
