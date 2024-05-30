"""
Module for handling the mysql database queries
"""

from datetime import date
import mysql.connector as mcn
from mysql.connector import errorcode


class db:
    def __init__(self):
        self.cnx = mcn.connect(
            host="localhost",
            user="root",
            password="!@#ItsRoot009",
            database="apostasmvp",
        )

        self.cursor = self.cnx.cursor()

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

    def insert_data(self, table_name, topic, date_created, daydelta):
        """
        Insert data into table
        """

        command = f"INSERT INTO {table_name} (topic, date_created, daydelta) VALUES (%s %s %s);"
        data = (topic, date_created, daydelta)
        try:
            self.cursor.execute(command, data)
        except mcn.Error as err:
            print("Value insertion was unsuccesful")
            print(err.msg)

    def query_db(self, table_name, query="*") -> list:
        command = f"SELECT {query} FROM {table_name};"
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return data

    def close_connection(self) -> None:
        self.cursor.close()
        self.cnx.close()
