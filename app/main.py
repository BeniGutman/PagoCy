from fastapi import FastAPI
from api.endpoints import resources, scans

app = FastAPI()

# Include routes for resources and scans
app.include_router(resources.router, prefix="/api")
app.include_router(scans.router, prefix="/api")

# Run the server: uvicorn main:app --reload --port 8000
