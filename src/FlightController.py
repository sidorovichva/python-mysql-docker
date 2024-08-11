from fastapi import APIRouter

from src.Flight import Flight
from src.FlightService import FlightService

router = APIRouter(prefix="/flight")


@router.post("/add")
async def add(flight: Flight) -> None:
    FlightService.add(flight)


@router.get("/get")
async def get() -> list[Flight]:
    return FlightService.get()
