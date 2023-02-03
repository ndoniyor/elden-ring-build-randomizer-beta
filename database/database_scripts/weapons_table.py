import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/items.db'

#id,name,image,description,attack,defence,scalesWith,requiredAttributes,category,weight
weapons_connection = sql.connect(db_path)
weapons_c = weapons_connection.cursor()
weapons_c.execute('''CREATE TABLE weapons (name)''')

weapons_csv = pd.read_csv('../csv/weapons.csv')
weapons_csv = weapons_csv.drop(["image"],axis=1)

weapons_csv.to_sql('weapons',weapons_connection, if_exists='replace', index=False)

