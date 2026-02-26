from app.core.db import events_db

class EventRepository:
    def __init__(self):
        self._events = events_db

    def save(self, event_data: dict):
        event_data["id"] = len(self._events) + 1
        self._events.append(event_data)
        return event_data

    def get_all(self):
        return self._events

    def find_by_id(self, event_id: int):
        for event in self._events:
            if event["id"] == event_id:
                return event
        return None

    def filter_by_location(self, location: str):
        return [e for e in self._events if e["location"].lower() == location.lower()]