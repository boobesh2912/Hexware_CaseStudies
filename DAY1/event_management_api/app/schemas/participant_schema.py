from pydantic import BaseModel, EmailStr, Field

class ParticipantBase(BaseModel):
    name: str = Field(..., min_length=2)
    email: str 
    event_id: int

class ParticipantCreate(ParticipantBase):
    pass

class ParticipantResponse(ParticipantBase):
    id: int

    class Config:
        from_attributes = True