from sqlalchemy import Column, String, DateTime

from src.config.DbSession import Base
from src.model.Flight import Flight
from src.table.Entity import Entity
from src.utils.Utils import Utils


class FlightEntity(Base, Entity):
    __tablename__ = 'flights'

    id = Column(String(length=255), primary_key=True, nullable=False)
    flight_number = Column(String(length=10))
    departure_airport = Column(String(length=5))
    departure_time = Column(DateTime)

    def add(self, session, o: Flight):
        return FlightEntity(
            id=Utils.generate_uuid(),
            flight_number=o.flight_number,
            departure_airport=o.departure_airport,
            departure_time=o.departure_time
        )
