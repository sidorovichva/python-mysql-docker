import os
import uuid

import mysql.connector as mysql
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from src.config.MySqlConnector import MySqlConnector


class MySqlConfig(MySqlConnector):

    @classmethod
    def session(cls) -> PooledMySQLConnection | MySQLConnectionAbstract:
        try:
            return mysql.connect(
                host=MySqlConnector.host(),
                user=MySqlConnector.username(),
                password=MySqlConnector.password(),
                database=MySqlConnector.database()
            )
        except mysql.Error as e:
            print(f"Error: {e}")

    # @classmethod
    # def add(cls, db: str, d: dict):
    #     cursor = cls.session().cursor()
    #     cursor.execute(
    #         f"INSERT INTO {db} (id, flight_number, departure_airport, departure_time) VALUES (%s, %s, %s, %s)",
    #         (cls.generate_uuid(), flight.flight_number, flight.departure_airport, flight.departure_time)
    #     )
    #     cls.session().close()
