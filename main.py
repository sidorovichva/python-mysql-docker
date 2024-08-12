from fastapi import FastAPI

from src.controller import FlightsController

app = FastAPI()
app.include_router(FlightsController.router)



