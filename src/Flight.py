from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel


@dataclass
class Flight(BaseModel):
    airline: str
    flight_number: str
    departure_city: str
    arrival_city: str
    departure_time: datetime
    arrival_time: datetime
    