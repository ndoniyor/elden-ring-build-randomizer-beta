import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/items.db'
    
armor_connection = sql.connect(db_path)
armor_c = armor_connection.cursor()
armor_c.execute('''CREATE TABLE armor_sets (name, category)''')

armor_csv = pd.read_csv('../csv/armor_sets.csv')

armor_csv.to_sql('armor_sets',armor_connection, if_exists='replace', index=False)
