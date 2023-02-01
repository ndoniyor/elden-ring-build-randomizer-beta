import sqlite3 as sql

def retrieve_data(db_file, table):
    conn = sql.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT * FROM "+table)
    data=c.fetchall()
    conn.close()
    return data

def insert_data(data, table_name):
    conn = sql.connect('../db/items.db')
    c=conn.cursor()
    c.executemany(f"INSERT INTO {table_name} VALUES (?)",data)
    conn.commit()
    conn.close()


armors = retrieve_data("../db/armors.db","armors")
ashes = retrieve_data("../db/ashes.db","ashes")
classes = retrieve_data("../db/classes.db","classes")
incantations = retrieve_data("../db/incantations.db","incantations")
shields = retrieve_data("../db/shields.db","shields")
sorceries = retrieve_data("../db/sorceries.db","sorceries")
#talismans = retrieve_data("../db/talismans.db","talismans")
weapons = retrieve_data("../db/weapons.db","weapons")

#insert_data(armors, "armors")
insert_data(ashes, "ashes")
insert_data(classes, "classes")
insert_data(incantations, "incantations")
insert_data(shields, "shields")
insert_data(sorceries, "sorceries")
insert_data(weapons, "weapons")

