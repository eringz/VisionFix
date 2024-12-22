from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Import settings from your config
from app.config.Settings import settings 

# Fetch DATABASE_URL from the settings
DATABASE_URL = settings.DATABASE_URL

# Initialize the database engine session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
