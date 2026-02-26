from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.exceptions.custom_exceptions import UserNotFoundException, UserAlreadyExistsException
import hashlib

# Service layer: business logic only
# Calls repository for DB access, raises custom exceptions

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def _hash_password(self, password: str) -> str:
        # Simple hash - in production use bcrypt or passlib
        return hashlib.sha256(password.encode()).hexdigest()

    def create_user(self, user_data: dict):
        # Business rule: prevent duplicate email
        existing = self.user_repo.get_user_by_email(user_data["email"])
        if existing:
            raise UserAlreadyExistsException(user_data["email"])

        # Hash the password before storing - never store plain text
        user_data["hashed_password"] = self._hash_password(user_data.pop("password"))
        return self.user_repo.create_user(user_data)

    def get_user(self, user_id: int):
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise UserNotFoundException(user_id)
        return user

    def get_all_users(self, skip: int = 0, limit: int = 10):
        return self.user_repo.get_all_users(skip, limit)

    def update_user(self, user_id: int, update_data: dict):
        user = self.get_user(user_id)   # reuse get_user which already raises if not found
        # Remove None values - don't overwrite existing data with None
        filtered = {k: v for k, v in update_data.items() if v is not None}
        return self.user_repo.update_user(user, filtered)

    def delete_user(self, user_id: int):
        user = self.get_user(user_id)
        self.user_repo.delete_user(user)