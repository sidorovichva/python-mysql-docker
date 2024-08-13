from src.config.Connector import Connector
from src.factory.ConnectorFactory import ConnectorFactory
from src.model.Flight import Flight


class FlightsService:

    def __init__(self):
        self.__connector: Connector = ConnectorFactory.get()

    @property
    def connector(self):
        return self.__connector

    def add(self, flight: Flight) -> str:
        return self.connector.add(flight)

    def get(self):
        return self.connector.get(Flight)
