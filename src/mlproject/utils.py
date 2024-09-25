import os
import sys

# Add the path to the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from mlproject.exception import CustomException
from mlproject.exception import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv("database")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        logging.info("Connection established",mydb)
        df=pd.read_sql_query('select * from zomato', mydb)
        print(df.head())

        return df

    except Exception as ex:
        raise CustomException(ex,sys)
