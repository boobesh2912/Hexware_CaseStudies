from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.participant_schema import ParticipantCreate, ParticipantResponse
from app.services.participant_service import ParticipantService
from app.dependencies.service_dependency import get_participant_service

router = APIRouter(prefix="/participants", tags=["Participants"])

@router.post("", response_model=ParticipantResponse, status_code=status.HTTP_201_CREATED)
def register_participant(data: ParticipantCreate, service: ParticipantService = Depends(get_participant_service)):
    result = service.register_participant(data.model_dump())
    if result == "EVENT_NOT_FOUND":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    if result == "CAPACITY_EXCEEDED":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Event capacity is full")
    if result == "EMAIL_ALREADY_REGISTERED":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return result

@router.get("/{participant_id}", response_model=ParticipantResponse, status_code=status.HTTP_200_OK)
def get_participant(participant_id: int, service: ParticipantService = Depends(get_participant_service)):
    participant = service.get_participant_by_id(participant_id)
    if not participant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participant not found")
    return participant