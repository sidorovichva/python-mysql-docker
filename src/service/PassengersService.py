from src.config.MySqlConnector import MySqlConnector
from src.factory.MySqlConnectorFactory import MySqlConnectorFactory
from src.model.Passenger import Passenger


class PassengersService:

    def __init__(self):
        self.__connector: MySqlConnector = MySqlConnectorFactory.get()

    @property
    def connector(self):
        return self.__connector

    def add(self, passenger: Passenger) -> str:
        return self.connector.add(passenger)
