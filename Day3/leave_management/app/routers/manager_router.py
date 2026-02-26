from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.dependencies.rbac import role_required
from app.controllers.manager_controller import ManagerController
from app.schemas.leave_schema import LeaveUpdate, LeaveResponse

router = APIRouter(prefix="/manager", tags=["Manager"])

@router.put("/leaves/{leave_id}", response_model=LeaveResponse)
def review_leave(leave_id: int, update: LeaveUpdate, db: Session = Depends(get_db), user=Depends(role_required("MANAGER"))):
    return ManagerController.update_leave_status(db, leave_id, update.status, user)