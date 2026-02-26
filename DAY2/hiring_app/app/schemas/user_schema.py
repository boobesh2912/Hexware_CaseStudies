from pydantic import BaseModel, EmailStr, Field
from app.models.user import UserRole

# Base has shared fields
class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., min_length=5)
    role: UserRole = UserRole.candidate

# UserCreate is used when POST /users — includes password
class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

# UserResponse is what we return — NEVER return hashed_password to client
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # allows SQLAlchemy ORM objects to auto-convert to this schema