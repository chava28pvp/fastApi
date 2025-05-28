from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    user_name: str = Field(alias="UserName")
    email: EmailStr
    role_id: int = Field(alias="RoleId")

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id_user: int = Field(alias="IdUser")
    created_at: datetime = Field(alias="CreatedAt")

    class Config:
        from_attributes = True  # Pydantic v2
        populate_by_name = True
