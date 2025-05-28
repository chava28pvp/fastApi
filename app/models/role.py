from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Role(Base):
    __tablename__ = "Roles"

    IdRole = Column(Integer, primary_key=True, index=True)
    Role = Column(String, nullable=False, unique=True)

    Users = relationship("User", back_populates="Roles")
