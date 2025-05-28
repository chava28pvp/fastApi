from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role import RoleCreate

def create_role(db: Session, role: RoleCreate):
    db_role = Role(Role=role.role)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_roles(db: Session):
    return db.query(Role).all()

def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.IdRole == role_id).first()