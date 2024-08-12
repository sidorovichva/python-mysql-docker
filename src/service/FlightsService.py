from src.config.MySqlConnector import MySqlConnector
from src.factory.MySqlConnectorFactory import MySqlConnectorFactory
from src.model.Flight import Flight
from src.table.FlightEntity import FlightEntity


class FlightsService:

    def __init__(self):
        self.__connector: MySqlConnector = MySqlConnectorFactory.get()

    @property
    def connector(self):
        return self.__connector

    def add(self, flight: Flight) -> str:
        return self.connector.add(flight)

    # def get(self) -> None:
    #     connection: PooledMySQLConnection | MySQLConnectionAbstract = MySqlConfig.get_connection()
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT * FROM flights")
    #     flights = cursor.fetchall()
    #     connection.close()
