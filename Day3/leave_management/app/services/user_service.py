from sqlalchemy.orm import Session
from app.repositories.user_repo import get_all_users, get_user_by_id
from app.core.pagination import paginate_query

def list_all_users_service(db: Session, page: int, size: int):
    query = get_all_users(db)
    return paginate_query(query, page, size)

def get_user_service(db: Session, user_id: int):
    return get_user_by_id(db, user_id)