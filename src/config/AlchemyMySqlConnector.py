import sqlalchemy
from pydantic import BaseModel
from sqlalchemy.orm import registry, Session

from src.config.EntityBaseModel import EntityBaseModel
from src.config.MySqlConnector import MySqlConnector


class AlchemyMySqlConnector(MySqlConnector):

    # def __init__(self):
    #     registry().generate_base().metadata.create_all(self.get_connection())

    @classmethod
    def get_connection(cls):
        username: str = MySqlConnector.username()
        password: str = MySqlConnector.password()
        host: str = MySqlConnector.host()
        database: str = MySqlConnector.database()
        port: str = MySqlConnector.port()
        return sqlalchemy.create_engine(
            url=f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}',
            echo=True
        )

    @classmethod
    def session(cls) -> Session:
        return Session(bind=cls.get_connection())

    @classmethod
    def add(cls, o: EntityBaseModel) -> str:
        session = cls.session()
        entity = o.to_entity()
        session.add(entity)
        session.flush()
        session.commit()
        return str(entity)
