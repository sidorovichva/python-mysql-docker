from src.config.MySqlConnector import MySQLConnector
from src.config.Connector import Connector


class ConnectorFactory:

    @classmethod
    def get(cls) -> Connector:
        return MySQLConnector()
