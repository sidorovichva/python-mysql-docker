from fastapi import FastAPI

from src.FlightController import FlightController

app = FastAPI()
app.include_router(FlightController.router)
