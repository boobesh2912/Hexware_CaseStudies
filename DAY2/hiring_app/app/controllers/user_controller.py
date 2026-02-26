from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserResponse

# prefix="/users" means all routes here start with /users automatically
router = APIRouter(prefix="/users", tags=["Users"])

# POST /users - Create user
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # Pydantic validates the request body before this even runs
    # db is injected by get_db dependency
    service = UserService(db)
    return service.create_user(user_data.model_dump())

# GET /users - List all users (with pagination)
@router.get("/", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    # Query params: GET /users?skip=0&limit=10
    service = UserService(db)
    return service.get_all_users(skip, limit)

# GET /users/{user_id} - Get user by path param
@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user(user_id)

# PUT /users/{user_id} - Update user
@router.put("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.update_user(user_id, user_data.model_dump())

# DELETE /users/{user_id} - Delete user
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    service.delete_user(user_id)