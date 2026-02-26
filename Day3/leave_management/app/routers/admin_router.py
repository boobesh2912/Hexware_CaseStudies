from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import role_required
from app.controllers.admin_controller import AdminController
from app.schemas.department_schema import DepartmentCreate, DepartmentResponse
from app.core.pagination import paginate_params

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/departments", response_model=DepartmentResponse)
def create_department(dept: DepartmentCreate, db: Session = Depends(get_db), user=Depends(role_required("ADMIN"))):
    return AdminController.create_department(db, dept.dict())

@router.get("/users")
def list_users(pagination: dict = Depends(paginate_params), db: Session = Depends(get_db), user=Depends(role_required("ADMIN"))):
    return AdminController.get_all_users(db, pagination["page"], pagination["size"])