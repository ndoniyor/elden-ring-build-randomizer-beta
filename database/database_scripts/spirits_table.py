import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/spirits.db'

if(path.exists(db_path)):
    remove(db_path)

#id,name,image,description,fpCost,hpCost,effect
spirits_connection = sql.connect('../db/spirits.db')
spirits_c = spirits_connection.cursor()
spirits_c.execute('''CREATE TABLE spirits (name)''')

spirits_csv = pd.read_csv('../csv/spirits.csv')
spirits_csv = spirits_csv.drop(["id","image","description","fpCost", "hpCost", "effect"],axis=1)

spirits_csv.to_sql('spirits',spirits_connection, if_exists='replace', index=False)

