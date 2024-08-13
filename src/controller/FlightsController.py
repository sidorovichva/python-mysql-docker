from fastapi import APIRouter
from starlette import status

from src.model.Flight import Flight
from src.service.FlightsService import FlightsService

router = APIRouter(prefix="/flights")


@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add(flight: Flight) -> str:
    return FlightsService().add(flight)


@router.get("/get")
async def get():
    return FlightsService().get()
