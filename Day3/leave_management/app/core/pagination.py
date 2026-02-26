from fastapi import Query
from app.core.config import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE

def paginate_params(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE, description="Items per page")
):
    size = min(size, MAX_PAGE_SIZE)
    return {"page": page, "size": size}

def paginate_query(query, page: int, size: int):
    total = query.count()
    items = query.offset((page - 1) * size).limit(size).all()
    return {
        "total": total,
        "page": page,
        "size": size,
        "items": items
    }