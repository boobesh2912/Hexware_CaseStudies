from sqlalchemy.orm import Session
from app.models.repayment import Repayment

class RepaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_repayment(self, repayment_data: dict) -> Repayment:
        new_repayment = Repayment(**repayment_data)
        self.db.add(new_repayment)
        try:
            self.db.commit()
        except:
            self.db.rollback()
            raise
        self.db.refresh(new_repayment)
        return new_repayment

    def get_repayments_by_loan(self, loan_application_id: int):
        return self.db.query(Repayment).filter(
            Repayment.loan_application_id == loan_application_id
        ).all()

    def get_total_paid(self, loan_application_id: int) -> float:
        repayments = self.get_repayments_by_loan(loan_application_id)
        return sum(r.amount_paid for r in repayments)