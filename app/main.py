from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import resources, scans

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allows specified origins
    allow_credentials=True,  # Allows cookies to be sent along with requests
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers (e.g., Authorization, Content-Type)
)

# Include routes for resources and scans
app.include_router(resources.router, prefix="/api")
app.include_router(scans.router, prefix="/api")

# Run the server: uvicorn main:app --reload --port 8000
