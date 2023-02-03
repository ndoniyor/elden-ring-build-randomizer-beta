import random
import sqlite3 as sql

DATABASE_DIR = "database/db/items.db"
SELECTION_STR = "SELECT * FROM "

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
        self.weapons = ""

    def choose_class(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR+"classes")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.starting_class=random_row[0]
        conn.close()

    def choose_armor(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR+"armors WHERE category='Helm'")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.helmet=random_row[0]

        cursor.execute(SELECTION_STR+"armors WHERE category='Chest Armor'")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.chest_armor=random_row[0]

        cursor.execute(SELECTION_STR+"armors WHERE category='Gauntlets'")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.gauntlets=random_row[0]

        cursor.execute(SELECTION_STR+"armors WHERE category='Leg Armor'")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.leg_armor=random_row[0]
        conn.close()

    def choose_ash_of_war(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR+"ashes")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.ash_of_war=random_row[0]
        conn.close()

    def choose_shield(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR+"shields")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.shield=random_row[0]
        conn.close()

    # def choose_spells(self):
    #     if(self.build_type == "S"):
    #         conn = sql.connect(DATABASE_DIR+"shields.db")
    #         cursor = conn.cursor()

    #         cursor.execute(SELECTION_STR+"shields")
    #         rows = cursor.fetchall()

    #         random_row = random.choice(rows)
    #         self.spells=random_row[0]
    #         conn.close()
        
    def choose_weapons(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR+"weapons")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.weapons=random_row[0]
        conn.close()

    def choose_all(self):
        self.choose_class()
        self.choose_armor()
        self.choose_weapons()