from sqlalchemy.orm import Session
from app.models.user import User

# Repository layer: ONLY talks to the database
# No business logic here - just raw CRUD operations

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: dict) -> User:
        new_user = User(**user_data)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)   # refresh fetches the new id assigned by DB
        return new_user

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_all_users(self, skip: int = 0, limit: int = 10):
        # Pagination: skip = offset (start from), limit = how many records to return
        return self.db.query(User).offset(skip).limit(limit).all()

    def update_user(self, user: User, update_data: dict) -> User:
        for key, value in update_data.items():
            setattr(user, key, value)   # dynamically update only provided fields
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()