from pydantic import BaseModel, Field

class RoleBase(BaseModel):
    role: str = Field(alias="Role")

class RoleCreate(RoleBase):
    pass

class RoleRead(RoleBase):
    id_role: int = Field(alias="IdRole")

    class Config:
        from_attributes = True
        populate_by_name = True
