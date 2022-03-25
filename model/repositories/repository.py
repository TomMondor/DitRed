import pymysql.cursors
import os
from dotenv import load_dotenv


class Repository:
    def __init__(self):
        load_dotenv()
        SQL_USER = os.getenv('SQL_USER')
        SQL_PASSWORD = os.getenv('SQL_PASSWORD')
        connection = pymysql.connect(
            host="localhost", user=SQL_USER, password=SQL_PASSWORD, db="DitRed", autocommit=True
        )
        self.cursor = connection.cursor()