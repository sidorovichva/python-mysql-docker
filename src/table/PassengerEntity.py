from sqlalchemy import Column, String, Date

from src.config.MySqlConnector import MySQLConnector, Base


class PassengerEntity(Base):
    __tablename__ = 'passengers'

    id = Column(String(length=255), primary_key=True, nullable=False)
    first_name = Column(String(length=255))
    last_name = Column(String(length=255))
    passport_number = Column(String(length=255))
    dob = Column(Date)

    def __repr__(self):
        return (f"PassengerEntity(id={self.id}, first_name={self.first_name},"
                f" last_name={self.last_name}, passport_number={self.passport_number}, dob={self.dob})")


Base.metadata.create_all(MySQLConnector.get_connection())
