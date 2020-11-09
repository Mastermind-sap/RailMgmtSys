"""
This will manage the database
"""
from __future__ import (print_function, absolute_import, with_statement)
import sqlite3


class MakeDb:
    """This class contains methods which creates and populates the database."""
    def __init__(self, dbname):
        self.dbname = dbname
        self.mydb = sqlite3.connect(self.dbname + '.db')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS DATA (TRAINID TEXT , TRAIN_NAME TEXT , JOURNEY TEXT ,TIMING TEXT)""")

    def store_values(self, TRAINID, TRAIN_NAME, JOURNEY, TIMING):
        "This method stores values in the database"

        self.cursor.execute("INSERT INTO DATA VALUES( {TRAINID} ,{TRAIN_NAME}, {JOURNEY}, {TIMING})")
        self.mydb.commit()

    def check_dup(self, TRAINID, TRAIN_NAME, JOURNEY, TIMING):
        self.cursor.execute(f"SELECT COUNT (*) FROM DATA WHERE TRAINID={TRAINID} AND TRAIN_NAME={TRAIN_NAME} AND JOURNEY={JOURNEY} AND TIMING={TIMING}")
        return self.cursor.fetchall()


class GetResponse(MakeDb):
    """This class will handle the responses for the database."""

    def __init__(self, Database):
        self.Database = Database
        super().__init__(Database)

    def get_data_by_query(self , query):
        self.query = query

        try:
            self.cursor.execute(
                f'SELECT *FROM DATA WHERE  TRAINID= {self.query}')

            data = self.cursor.fetchall()
            return data
        except:
            return 'No Such Query Available Available'

    def get_all_data(self):
        self.cursor.execute("Select * FROM DATA")
        data = self.cursor.fetchall()
        return(data)

    def delete_data(self, TRAINID, TRAIN_NAME, JOURNEY, TIMING):
        self.cursor.execute(f"DELETE FROM DATA WHERE TRAINID={TRAINID} AND TRAIN_NAME={TRAIN_NAME} AND JOURNEY={JOURNEY} AND TIMING={TIMING} LIMIT 1")
        self.mydb.commit()

# if __name__ == '__main__':
    # db = make_db('Databs')  # Enter Database name
    # db.store_values(12, 'Nick', 24)  # Enter Rollno,Studentname,marks
    # d = get_response('Databs', 'Nick').get_data()
    # print(d)





