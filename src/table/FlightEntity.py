from sqlalchemy import Column, String, DateTime

from src.config.MySqlConnector import MySQLConnector, Base


class FlightEntity(Base):
    __tablename__ = 'flights'

    id = Column(String(length=255), primary_key=True, nullable=False)
    flight_number = Column(String(length=10))
    departure_airport = Column(String(length=5))
    departure_time = Column(DateTime)

    def __repr__(self):
        return (f"FlightEntity(id={self.id}, flight_number={self.flight_number},"
                f" departure_airport={self.departure_airport}, departure_time={self.departure_time})")


Base.metadata.create_all(MySQLConnector.get_connection())
