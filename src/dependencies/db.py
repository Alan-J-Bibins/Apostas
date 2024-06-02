"""
Module for handling the mysql database queries
"""

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

    def update_data(self,table_name,col_name, col_value, update_criteria, update_criteria_value):
        command = f"UPDATE {table_name} SET {col_name} = {col_value} WHERE {update_criteria} = {update_criteria_value};"
        print(command)
        self.cursor.execute(command)
        self.cnx.commit()

    def query_db(self, table_name, query="*", where_section="") -> list:
        command = f"SELECT {query} FROM {table_name} {where_section};"
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return data

    def close_connection(self) -> None:
        self.cursor.close()
        self.cnx.close()
