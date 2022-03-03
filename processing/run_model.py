import pymysql
import pandas as pd
import os


dbcon = pymysql.connect("localhost", "root", "my-secret-pw", "tc_store_new")

try:
    SQL_Query = pd.read_sql_query(
        '''SELECT product_id, transaction_id, quantity
            FROM tc_store_new.order
                where
	        created_on > '2022-03-02';''', dbcon)
print(SQL_Query)