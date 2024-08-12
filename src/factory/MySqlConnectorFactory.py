from src.config.AlchemyMySqlConnector import AlchemyMySqlConnector
from src.config.MySqlConnector import MySqlConnector


class MySqlConnectorFactory:

    @classmethod
    def get(cls) -> MySqlConnector:
        return AlchemyMySqlConnector()
