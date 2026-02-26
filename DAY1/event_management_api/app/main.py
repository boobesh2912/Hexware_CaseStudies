from fastapi import FastAPI
from app.middleware.cors_middleware import add_cors_middleware
from app.controllers.event_controller import router as event_router
from app.controllers.participant_controller import router as participant_router

app = FastAPI(title="Event Management System API")

add_cors_middleware(app)

app.include_router(event_router)
app.include_router(participant_router)

@app.get("/")
def root():
    return {"message": "Event Management System API is running"}