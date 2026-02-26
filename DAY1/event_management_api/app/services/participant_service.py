class ParticipantService:
    def __init__(self, participant_repository, event_repository):
        self.participant_repository = participant_repository
        self.event_repository = event_repository

    def register_participant(self, participant_data: dict):
        # Business Rule 1: Event must exist [cite: 167, 354]
        event = self.event_repository.find_by_id(participant_data["event_id"])
        if not event:
            return "EVENT_NOT_FOUND"

        # Business Rule 2: Ensure event capacity is not exceeded [cite: 77, 168, 264, 355]
        # We check the current number of participants for this specific event
        current_participants = [
            p for p in self.participant_repository._participants 
            if p["event_id"] == participant_data["event_id"]
        ]
        
        if len(current_participants) >= event["capacity"]:
            return "CAPACITY_EXCEEDED"

        # Business Rule 3: Ensure participant email is unique [cite: 78, 169, 265, 356]
        if self.participant_repository.find_by_email(participant_data["email"]):
            return "EMAIL_ALREADY_REGISTERED"

        return self.participant_repository.save(participant_data)

    def get_participant_by_id(self, participant_id: int):
        return self.participant_repository.find_by_id(participant_id)