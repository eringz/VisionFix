from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Import settings from your config
from app.config.Settings import settings 

# Fetch DATABASE_URL from the settings
DATABASE_URL = settings.DATABASE_URL

# Initialize the database engine session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal() # Creates a new session
    try:
        yield db # Yields the session to the router handler
    finally:
        db.close() # Ensure that the session is closed after use