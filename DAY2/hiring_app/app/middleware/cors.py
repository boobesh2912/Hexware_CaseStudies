from fastapi.middleware.cors import CORSMiddleware

# CORS = Cross-Origin Resource Sharing
# Allows your frontend (running on a different port/domain) to call this API
# allow_origins=["*"] means any frontend can call - fine for development

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )