from dataclasses import dataclass
from datetime import datetime

from src.model.EntityBaseModel import EntityBaseModel
from src.table.FlightEntity import FlightEntity
from src.utils.Utils import Utils


@dataclass
class Flight(EntityBaseModel):
    flight_number: str
    departure_airport: str
    departure_time: datetime

    def to_entity(self) -> FlightEntity:
        return FlightEntity(
            id=Utils.generate_uuid(),
            flight_number=self.flight_number,
            departure_airport=self.departure_airport,
            departure_time=self.departure_time
        )
