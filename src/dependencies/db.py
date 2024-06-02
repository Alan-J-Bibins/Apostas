"""
Module for handling the mysql database queries
"""

import dependencies.config_db as cdb
import mysql.connector as mcn
from mysql.connector import errorcode


class db:
    def __init__(self):
        self.cnx = mcn.connect(
            host=cdb.host,
            user=cdb.user,
            password=cdb.password,
        )

        self.cursor = self.cnx.cursor()

    def connect_to_db(self, DB_NAME):
        try:
            self.cursor.execute("USE {}".format(DB_NAME))
        except mcn.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_db(DB_NAME)
                print("Database {} created successfully.".format(DB_NAME))
                self.cursor.execute("USE {}".format(DB_NAME))
            else:
                print(err.msg)
                exit(1)

    def create_db(self, DB_NAME):
        try:
            self.cursor.execute("CREATE DATABASE {};".format(DB_NAME))
        except mcn.Error as err:
            print("Failed to create Database")
            print(err.msg)

    def create_table(self, table_name, table_description) -> None:
        """
        Create table
        """
        try:
            self.cursor.execute(f"CREATE TABLE {table_name} ({table_description});")
            print("Table created succesfully")
        except mcn.Error as err:
            if err.errno != errorcode.ER_TABLE_EXISTS_ERROR:
                print(err.msg)

    def insert_data(
        self, table_name: str, topic: str, date_created: str, daydelta: int
    ):
        """
        Insert data into table
        """

        command = f"INSERT INTO {table_name} (topic, date_created, daydelta) VALUES (%s, %s, %s);"
        data = (topic, date_created, daydelta)
        try:
            self.cursor.execute(command, data)
            self.cnx.commit()
        except mcn.Error as err:
            print("Value insertion was unsuccesful")
            print(err.msg)

    def update_data(
        self, table_name, col_name, col_value, update_criteria, update_criteria_value
    ):
        command = f"UPDATE {table_name} SET {col_name} = {col_value} WHERE {update_criteria} = {update_criteria_value};"
        try:
            self.cursor.execute(command)
            self.cnx.commit()
        except mcn.Error as err:
            print(err.msg)

    def query_db(self, table_name, query="*", where_section="") -> list:
        command = f"SELECT {query} FROM {table_name} {where_section};"
        data = []
        try:
            self.cursor.execute(command)
            data = self.cursor.fetchall()
        except mcn.Error as err:
            print(err.msg)
        return data

    def close_connection(self) -> None:
        try:
            self.cursor.close()
            self.cnx.close()
        except mcn.Error as err:
            print(err.msg)
