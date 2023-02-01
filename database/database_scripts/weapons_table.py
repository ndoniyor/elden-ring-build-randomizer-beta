import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/weapons.db'

if(path.exists(db_path)):
    remove(db_path)

#id,name,image,description,attack,defence,scalesWith,requiredAttributes,category,weight
weapons_connection = sql.connect('../db/weapons.db')
weapons_c = weapons_connection.cursor()
weapons_c.execute('''CREATE TABLE weapons (name)''')

weapons_csv = pd.read_csv('../csv/weapons.csv')
weapons_csv = weapons_csv.drop(["id","image","description","attack", "defence", "scalesWith", "requiredAttributes", "category", "weight"],axis=1)

weapons_csv.to_sql('weapons',weapons_connection, if_exists='replace', index=False)

