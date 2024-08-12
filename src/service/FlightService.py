from src.config.DefaultMySQLConnector import MySqlConfig
from src.config.MySqlConnector import MySqlConnector
from src.factory.MySqlConnectorFactory import MySqlConnectorFactory
from src.model.Flight import Flight
from src.table.FlightEntity import FlightEntity
from src.utils.Utils import Utils


class FlightService:

    def __init__(self):
        self.__table = "flights"
        self.__connector: MySqlConnector = MySqlConnectorFactory.get()

    @property
    def table(self) -> str:
        return self.__table

    @property
    def connector(self):
        return self.__connector

    def add(self, flight: Flight) -> None:
        session = self.connector.session()

        session.add(FlightEntity(
            id=Utils.generate_uuid(),
            flight_number=flight.flight_number,
            departure_airport=flight.departure_airport,
            departure_time=flight.departure_time
        ))

        session.flush()
        session.commit()

    # def get(self) -> None:
    #     connection: PooledMySQLConnection | MySQLConnectionAbstract = MySqlConfig.get_connection()
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT * FROM flights")
    #     flights = cursor.fetchall()
    #     connection.close()
