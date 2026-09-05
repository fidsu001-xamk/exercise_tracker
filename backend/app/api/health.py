from fastapi import APIRouter

from app.schemas.health import HealthResponse
from app.services.health import gethealth

router = APIRouter()

@router.get("/health", response_model=HealthResponse, tags=["health"])
def health_check() -> HealthResponse:
    return HealthResponse(status=gethealth())
