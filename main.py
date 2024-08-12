from fastapi import FastAPI

from src.controller import FlightsController, PassengersController

app = FastAPI()
app.include_router(FlightsController.router)
app.include_router(PassengersController.router)



