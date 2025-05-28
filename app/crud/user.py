from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from datetime import datetime
from passlib.context import CryptContext
from sqlalchemy import asc  # For ordering

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        UserName=user.user_name,
        email=user.email,
        PasswordHash=hashed_password,
        CreatedAt=datetime.utcnow(),
        RoleId=user.role_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).order_by(asc(User.IdUser)).offset(skip).limit(limit).all()