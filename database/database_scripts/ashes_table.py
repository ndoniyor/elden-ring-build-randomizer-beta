import sqlite3 as sql
import pandas as pd
from os import remove, path

db_path = '../db/ashes.db'

if(path.exists(db_path)):
    remove(db_path)

ashes_connection = sql.connect('../db/ashes.db')
ashes_c = ashes_connection.cursor()
ashes_c.execute('''CREATE TABLE ashes (name, description)''')

ashes_csv = pd.read_csv('../csv/ashes.csv')
ashes_csv = ashes_csv.drop(["image","affinity"],axis=1)

ashes_csv.to_sql('ashes',ashes_connection, if_exists='replace', index=False)

