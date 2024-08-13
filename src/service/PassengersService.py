from src.config.Connector import Connector
from src.factory.ConnectorFactory import ConnectorFactory
from src.model.Passenger import Passenger


class PassengersService:

    def __init__(self):
        self.__connector: Connector = ConnectorFactory.get()

    @property
    def connector(self):
        return self.__connector

    def add(self, passenger: Passenger) -> str:
        return self.connector.add(passenger)

    def get(self):
        return self.connector.get(Passenger)
