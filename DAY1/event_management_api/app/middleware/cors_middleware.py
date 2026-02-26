from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    # This matches the configuration found in library_api/app/middleware/cors.py
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins as per training example
        allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allows all headers
        allow_credentials=True,
    )