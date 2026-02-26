from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import role_required
from app.controllers.employee_controller import EmployeeController
from app.schemas.leave_schema import LeaveCreate, LeaveResponse
from app.core.pagination import paginate_params

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.post("/apply-leave", response_model=LeaveResponse)
def apply_leave(leave: LeaveCreate, db: Session = Depends(get_db), user=Depends(role_required("EMPLOYEE"))):
    return EmployeeController.apply_leave(db, user, leave.dict())

@router.get("/my-leaves")
def view_leaves(pagination: dict = Depends(paginate_params), db: Session = Depends(get_db), user=Depends(role_required("EMPLOYEE"))):
    return EmployeeController.get_my_leaves(db, user, pagination["page"], pagination["size"])