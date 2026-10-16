from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.adapters.mock_idsnext import MockIDSNextAdapter
from app.services.sync_service import sync_service

app = FastAPI(
    title="IDS Next Hotel Integration Demo",
    description="Simulated PMS integration using fictional hotel data",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Local demo only
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

pms = MockIDSNextAdapter()


@app.get("/")
def home():
    return {"message": "IDS Next Integration Demo", "mode": "simulation"}


@app.get("/api/{resource}")
def get_resource(resource: str):
    allowed = {"guests", "rooms", "reservations", "folios"}

    if resource not in allowed:
        raise HTTPException(status_code=404, detail="Resource not found")

    return {"source": "mock_idsnext", "data": pms.get_data(resource)}


@app.post("/api/sync/reservations")
def sync_reservations():
    return sync_service.sync_reservations()
