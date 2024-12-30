from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.Database import get_db
from app.controllers.UserController import get_users_from_db, get_user_by_email


router = APIRouter()

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    # Use the db session to query the database
    users = get_users_from_db(db) # Get Users from User Controller
    return users

@router.get("/user")
def get_user(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    return user

    