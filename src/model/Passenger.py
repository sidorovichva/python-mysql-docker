from dataclasses import dataclass
from datetime import date

from src.model.EntityBaseModel import EntityBaseModel
from src.table.PassengerEntity import PassengerEntity
from src.utils.Utils import Utils


@dataclass
class Passenger(EntityBaseModel):
    first_name: str
    last_name: str
    passport_number: str
    dob: date

    def to_entity(self) -> PassengerEntity:
        return PassengerEntity(
            id=Utils.generate_uuid(),
            first_name=self.first_name,
            last_name=self.last_name,
            passport_number=self.passport_number,
            dob=self.dob
        )