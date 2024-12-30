from sqlalchemy.orm import Session
from app.models.User import User

def create_user(db: Session, firstName: str, lastName: str, email: str, password: str):
    db_user = User(firstName=firstName, lastName=lastName, email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users_from_db(db: Session):
    return db.query(User).all()

