from app.repositories.event_repository import EventRepository
from app.repositories.participant_repository import ParticipantRepository
from app.services.event_service import EventService
from app.services.participant_service import ParticipantService

# We create singleton instances of the repositories here.
# This ensures that all services use the same in-memory data lists.
event_repo = EventRepository()
participant_repo = ParticipantRepository()

def get_event_service():
    # Injects the singleton event repository into the service
    return EventService(event_repo)

def get_participant_service():
    # Injects both repositories as required by the ParticipantService logic
    return ParticipantService(participant_repo, event_repo)