from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class User(Base):
    __tablename__ = "Users"

    IdUser = Column(Integer, primary_key=True, index=True)
    UserName = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    PasswordHash = Column(String, nullable=False)
    CreatedAt = Column(DateTime, default=datetime.utcnow)
    RoleId = Column(Integer, ForeignKey("Roles.IdRole"), nullable=False)

    Roles = relationship("Role", back_populates="Users")