
import os

import mysql.connector
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = 'swiftMarket'


connection = mysql.connector.connect(user = user,
                                     password = password,
                                     host = host,
                                    database = database )
cursor = connection.cursor()


def read_query(query):
    """"Reading SQL Queries Only For SELECT Queris
     REturns: Pd.DataFrame"""

    cursor.execute(query)
    rows = cursor.fetchall()
    return pd.DataFrame(data = rows , columns = cursor.column_names )


# if __name__=='__main__':