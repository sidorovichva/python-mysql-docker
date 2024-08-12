from fastapi import APIRouter
from starlette import status

from src.model.Flight import Flight
from src.model.Passenger import Passenger
from src.service.PassengersService import PassengersService

router = APIRouter(prefix="/passengers")


@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add(passenger: Passenger) -> str:
    return PassengersService().add(passenger)


@router.get("/get")
async def get() -> list[Flight]:
    return PassengersService().get()