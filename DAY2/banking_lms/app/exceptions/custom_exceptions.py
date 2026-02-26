class UserNotFoundException(Exception):
    def __init__(self, user_id: int):
        super().__init__(f"User with id {user_id} not found")

class UserAlreadyExistsException(Exception):
    def __init__(self, email: str):
        super().__init__(f"User with email '{email}' already exists")

class LoanProductNotFoundException(Exception):
    def __init__(self, product_id: int):
        super().__init__(f"Loan product with id {product_id} not found")

class LoanApplicationNotFoundException(Exception):
    def __init__(self, application_id: int):
        super().__init__(f"Loan application with id {application_id} not found")

class RepaymentNotFoundException(Exception):
    def __init__(self, repayment_id: int):
        super().__init__(f"Repayment with id {repayment_id} not found")

class LoanAmountExceededException(Exception):
    def __init__(self, requested: float, max_amount: float):
        super().__init__(f"Requested amount {requested} exceeds product max amount {max_amount}")

class UnauthorizedActionException(Exception):
    def __init__(self, message: str = "You are not authorized to perform this action"):
        super().__init__(message)

class InvalidLoanStatusException(Exception):
    def __init__(self, message: str):
        super().__init__(message)