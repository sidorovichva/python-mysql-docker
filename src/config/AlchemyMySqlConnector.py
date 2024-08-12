import sqlalchemy
from sqlalchemy.orm import Session, declarative_base

from src.model.EntityBaseModel import EntityBaseModel
from src.config.MySqlConnector import MySqlConnector

Base = declarative_base()


class AlchemyMySqlConnector(MySqlConnector):

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
