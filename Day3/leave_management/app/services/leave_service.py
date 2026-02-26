from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import date
from app.repositories.leave_repo import create_leave, get_leave_by_id, get_leaves_by_employee, update_leave
from app.core.pagination import paginate_query

def apply_leave_service(db: Session, user, leave_data: dict):
    # Validation: End date must be after start date
    if leave_data["end_date"] < leave_data["start_date"]:
        raise HTTPException(status_code=400, detail="End date cannot be before start date")

    # Business Logic: Check for overlapping leave requests for this employee
    existing_leaves = get_leaves_by_employee(db, user.id).all()
    for l in existing_leaves:
        if not (leave_data["end_date"] < l.start_date or leave_data["start_date"] > l.end_date):
            raise HTTPException(status_code=400, detail="Leave request overlaps with an existing one")

    leave_data["employee_id"] = user.id
    leave_data["status"] = "PENDING"
    return create_leave(db, leave_data)

def approve_reject_leave_service(db: Session, leave_id: int, status: str, manager):
    leave = get_leave_by_id(db, leave_id)
    if not leave:
        raise HTTPException(status_code=404, detail="Leave request not found")

    # Validation: Manager can only approve/reject leaves within their department
    if manager.role != "ADMIN" and leave.employee.department_id != manager.department_id:
        raise HTTPException(status_code=403, detail="Not authorized to manage this department's leaves")

    update_data = {"status": status, "approved_by": manager.id}
    return update_leave(db, leave, update_data)

def list_employee_leaves_service(db: Session, user_id: int, page: int, size: int):
    query = get_leaves_by_employee(db, user_id)
    return paginate_query(query, page, size)