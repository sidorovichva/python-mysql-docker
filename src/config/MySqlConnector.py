from typing import Type

import sqlalchemy
from sqlalchemy import select
from sqlalchemy.orm import Session, declarative_base

from src.model.EntityBaseModel import EntityBaseModel
from src.config.Connector import Connector

Base = declarative_base()


class MySQLConnector(Connector):

    @classmethod
    def get_connection(cls):
        username: str = Connector.username()
        password: str = Connector.password()
        host: str = Connector.host()
        database: str = Connector.database()
        port: str = Connector.port()
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

    @classmethod
    def get(
        cls, entity: Type[EntityBaseModel],
        equals: dict = None
    ):
        session = cls.session()
        query = select(entity.to_entity_class())

        if equals is not None:
            for key, value in equals.items():
                query = query.where(key == value)

        result = session.execute(query).scalars().all()
        return result
