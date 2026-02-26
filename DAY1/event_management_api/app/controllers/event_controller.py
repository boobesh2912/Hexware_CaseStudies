from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from app.schemas.event_schema import EventCreate, EventResponse
from app.services.event_service import EventService
from app.dependencies.service_dependency import get_event_service

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(data: EventCreate, service: EventService = Depends(get_event_service)):
    result = service.create_event(data.model_dump())
    if result is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Event with this name already exists")
    return result

@router.get("", response_model=List[EventResponse], status_code=status.HTTP_200_OK)
def get_events(location: Optional[str] = None, service: EventService = Depends(get_event_service)):
    return service.get_all_events(location)

@router.get("/{event_id}", response_model=EventResponse, status_code=status.HTTP_200_OK)
def get_event(event_id: int, service: EventService = Depends(get_event_service)):
    event = service.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return event