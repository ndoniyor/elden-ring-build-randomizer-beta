import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/classes.db'

if(path.exists(db_path)):
    remove(db_path)

classes_connection = sql.connect('../db/classes.db')
classes_c = classes_connection.cursor()
classes_c.execute('''CREATE TABLE classes (name)''')

classes_csv = pd.read_csv('../csv/classes.csv')
classes_csv = classes_csv.drop(["id","image","description","stats"],axis=1)

classes_csv.to_sql('classes',classes_connection, if_exists='replace', index=False)

