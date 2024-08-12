from abc import ABC, abstractmethod

from pydantic import BaseModel


class Entity(ABC):

    @abstractmethod
    def add(self, o: BaseModel):
        pass
