import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/items.db'


#id,name,image,description,fpCost,hpCost,effect
spirits_connection = sql.connect(db_path)
spirits_c = spirits_connection.cursor()
spirits_c.execute('''CREATE TABLE spirits (name)''')

spirits_csv = pd.read_csv('../csv/spirits.csv')

spirits_csv.to_sql('spirits',spirits_connection, if_exists='replace', index=False)

