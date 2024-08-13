from abc import ABC, abstractmethod
import os
from typing import Type

from src.model.EntityBaseModel import EntityBaseModel


class Connector(ABC):

    @classmethod
    def host(cls) -> str:
        return os.getenv("HOST")

    @classmethod
    def port(cls) -> str:
        return os.getenv("PORT")

    @classmethod
    def username(cls) -> str:
        return os.getenv("USERNAME")

    @classmethod
    def password(cls) -> str:
        return os.getenv("PASSWORD")

    @classmethod
    def database(cls) -> str:
        return os.getenv("DATABASE")

    @abstractmethod
    def session(self):
        pass

    @abstractmethod
    def add(self, o: EntityBaseModel) -> str:
        pass

    @abstractmethod
    def get(
            self, o: Type[EntityBaseModel],
            equals: dict = None
    ) -> list:
        pass
