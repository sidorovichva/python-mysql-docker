from abc import abstractmethod

from pydantic import BaseModel


class EntityBaseModel(BaseModel):

    @abstractmethod
    def to_entity(self):
        pass
