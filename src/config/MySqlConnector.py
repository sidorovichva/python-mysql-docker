import uuid
from abc import ABC, abstractmethod
import os

from pydantic import BaseModel


class MySqlConnector(ABC):

    @classmethod
    def host(cls) -> str:
        return os.getenv("host")

    @classmethod
    def port(cls) -> str:
        return os.getenv("port")

    @classmethod
    def username(cls) -> str:
        return os.getenv("username")

    @classmethod
    def password(cls) -> str:
        return os.getenv("password")

    @classmethod
    def database(cls) -> str:
        return os.getenv("database")

    @abstractmethod
    def session(self):
        pass
