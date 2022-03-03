import pymysql
import pandas as pd
import os


dbcon = pymysql.connect("localhost", "root", "my-secret-pw", "tc_store_new")

try:
    SQL_Query = pd.read_sql_query(
        '''select
          symptoms,
          country_name,
          cases
          from coronas''', dbcon)