from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.Database import get_db
from app.models.User import User

router = APIRouter()

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    # Use the db session to query the database
    users = db.query(User).all() # Fetch all users
    return users

    