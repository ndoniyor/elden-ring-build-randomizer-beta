import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/items.db'

#id,name,image,description,attack,defence,scalesWith,requiredAttributes,category,weight
shields_connection = sql.connect(db_path)
shields_c = shields_connection.cursor()
shields_c.execute('''CREATE TABLE shields (name)''')

shields_csv = pd.read_csv('../csv/shields.csv')

shields_csv.to_sql('shields',shields_connection, if_exists='replace', index=False)

