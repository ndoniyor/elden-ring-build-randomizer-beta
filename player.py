import random
import sqlite3 as sql

#TODO consider making an armor class to better distinguish between pure random and organized random
class Player:
    #starting_class, build_type, armor, ash_of_war, shield, spells
    def __init__(self):
        self.starting_class = ""
        self.build_type = ""
        self.helmet = ""
        self.chest_armor = ""
        self.gauntlets = ""
        self.leg_armor = ""
        self.ash_of_war = ""
        self.shield = ""
        self.spells = ""

    def choose_class(self):
        conn = sql.connect("database/db/classes.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM classes")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.starting_class=random_row[0]
        conn.close()

    def choose_armor(self):
        #TODO database parameter?
        conn = sql.connect("database/db/armors.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM armors WHERE category='Helmet'")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.helmet=random_row[0]

        cursor.execute("SELECT * FROM armors WHERE category='Chest Armor'")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.chest_armor=random_row[0]

        cursor.execute("SELECT * FROM armors WHERE category='Gauntlets'")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.gauntlets=random_row[0]

        cursor.execute("SELECT * FROM armors WHERE category='Leg Armor'")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.leg_armor=random_row[0]
        conn.close()