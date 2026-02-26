from typing import List, Optional

class EventService:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    def create_event(self, event_data: dict):
        # Business Rule: Prevent duplicate event names 
        all_events = self.event_repository.get_all()
        for event in all_events:
            if event["name"].lower() == event_data["name"].lower():
                return None
        
        return self.event_repository.save(event_data)

    def get_all_events(self, location: Optional[str] = None):
        if location:
            return self.event_repository.filter_by_location(location)
        return self.event_repository.get_all()

    def get_event_by_id(self, event_id: int):
        return self.event_repository.find_by_id(event_id)