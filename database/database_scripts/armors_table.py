import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/items.db'

if(path.exists(db_path)):
    remove(db_path)
    
armor_connection = sql.connect(db_path)
armor_c = armor_connection.cursor()
armor_c.execute('''CREATE TABLE armors (name, category)''')

armor_csv = pd.read_csv('../csv/armors.csv')
armor_csv = armor_csv.drop(["image"],axis=1)

armor_csv.to_sql('armors',armor_connection, if_exists='replace', index=False)
