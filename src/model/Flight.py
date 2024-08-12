from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel


@dataclass
class Flight(BaseModel):
    flight_number: str
    departure_airport: str
    departure_time: datetime
