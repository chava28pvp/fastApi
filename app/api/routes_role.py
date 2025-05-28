from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.role import RoleCreate, RoleRead
from app.crud.role import create_role, get_roles
from app.core.database import get_db

router = APIRouter(prefix="/roles", tags=["roles"])

@router.post("/", response_model=RoleRead)
def create_new_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)

@router.get("/", response_model=list[RoleRead])
def list_roles(db: Session = Depends(get_db)):
    return get_roles(db)
