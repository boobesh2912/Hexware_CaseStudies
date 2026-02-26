from app.core.db import participants_db

class ParticipantRepository:
    def __init__(self):
        self._participants = participants_db

    def save(self, participant_data: dict):
        participant_data["id"] = len(self._participants) + 1
        self._participants.append(participant_data)
        return participant_data

    def find_by_id(self, participant_id: int):
        for p in self._participants:
            if p["id"] == participant_id:
                return p
        return None

    def find_by_email(self, email: str):
        for p in self._participants:
            if p["email"] == email:
                return p
        return None