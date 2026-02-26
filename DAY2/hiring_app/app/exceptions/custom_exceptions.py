# Custom exception classes - each maps to a specific domain error
# This way your service layer raises meaningful exceptions
# instead of generic HTTPException everywhere

class UserNotFoundException(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id
        super().__init__(f"User with id {user_id} not found")

class UserAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"User with email '{email}' already exists")

class JobNotFoundException(Exception):
    def __init__(self, job_id: int):
        self.job_id = job_id
        super().__init__(f"Job with id {job_id} not found")

class ApplicationNotFoundException(Exception):
    def __init__(self, application_id: int):
        self.application_id = application_id
        super().__init__(f"Application with id {application_id} not found")

class AlreadyAppliedException(Exception):
    def __init__(self, user_id: int, job_id: int):
        super().__init__(f"User {user_id} has already applied for job {job_id}")