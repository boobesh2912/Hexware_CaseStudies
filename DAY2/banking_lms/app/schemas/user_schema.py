from pydantic import BaseModel, Field
from app.models.user import UserRole

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: str = Field(..., min_length=5)
    role: UserRole = UserRole.customer
    password: str = Field(..., min_length=6)

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole

    class Config:
        from_attributes = True