from sqlalchemy import Column, String, DateTime

from src.config.DbSession import Base


class FlightEntity(Base):
    __tablename__ = 'flights'

    id = Column(String(length=255), primary_key=True, nullable=False)
    flight_number = Column(String(length=10))
    departure_airport = Column(String(length=5))
    departure_time = Column(DateTime)

    def __str__(self):
        return (f"FlightEntity(id={self.id}, flight_number={self.flight_number},"
                f" departure_airport={self.departure_airport}, departure_time={self.departure_time})")
