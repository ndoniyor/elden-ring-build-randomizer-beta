import random
import sqlite3 as sql
import sys

DATABASE_DIR = "database/db/items.db"
SELECTION_STR = "SELECT * FROM "

# Build type flags:
# Melee/Int/Sorc

class Item:
    def __init__(self, name="", link=""):
        self.name = name
        self.link = link

    def setName(self, name):
        self.name = name

    def setLink(self, link):
        self.link = link


class Player:
    def __init__(self, ):
        self.starting_class = Item()
        self.build_flags = []
        self.helmet = Item()
        self.chest_armor = Item()
        self.gauntlets = Item()
        self.leg_armor = Item()
        self.ash_of_war = Item()
        self.shield = Item()
        self.spells = []
        self.weapons = Item()
        self.spirit_ash = Item()

    def choose_class(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR + "classes")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.starting_class.setName(random_row[0])
        self.starting_class.setLink(random_row[1])
        conn.close()

    def choose_armor(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        if "armor_sets" in self.build_flags:
            cursor.execute(SELECTION_STR + "armor_sets")
            rows = cursor.fetchall()
            random_row = random.choice(rows)

            self.helmet.setName(random_row[0])
            self.helmet.setLink(random_row[1])
        else:
            cursor.execute(SELECTION_STR + "armors WHERE category='Helm'")
            rows = cursor.fetchall()

            random_row = random.choice(rows)
            self.helmet.setName(random_row[0])
            self.helmet.setLink(random_row[1])

            cursor.execute(SELECTION_STR + "armors WHERE category='Chest Armor'")
            rows = cursor.fetchall()

            random_row = random.choice(rows)
            self.chest_armor.setName(random_row[0])
            self.chest_armor.setLink(random_row[1])

            cursor.execute(SELECTION_STR + "armors WHERE category='Gauntlets'")
            rows = cursor.fetchall()

            random_row = random.choice(rows)
            self.gauntlets.setName(random_row[0])
            self.gauntlets.setLink(random_row[1])

            cursor.execute(SELECTION_STR + "armors WHERE category='Leg Armor'")
            rows = cursor.fetchall()

            random_row = random.choice(rows)
            self.leg_armor.setName(random_row[0])
            self.leg_armor.setLink(random_row[1])
        conn.close()

    def choose_ash_of_war(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR + "ashes")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.ash_of_war.setName(random_row[0])
        self.ash_of_war.setLink(random_row[1])
        conn.close()

    def choose_shield(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR + "shields")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.shield.setName(random_row[0])
        self.shield.setLink(random_row[1])
        conn.close()

    def choose_spirit_ash(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR + "spirits")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.spirit_ash.setName(random_row[0])
        self.spirit_ash.setLink(random_row[1])
        conn.close()

    def choose_spells(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()
        if "S" in self.build_flags:
            cursor.execute("SELECT * FROM sorceries ORDER BY RANDOM() LIMIT 5")
            rows = cursor.fetchall()
        elif "I" in self.build_flags:
            cursor.execute("SELECT * FROM incantations ORDER BY RANDOM() LIMIT 5")
            rows = cursor.fetchall()
        for spell in rows:
            self.spells.append(Item(spell[0],spell[1]))
        conn.close()


    def choose_weapons(self):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR + "weapons")
        rows = cursor.fetchall()

        random_row = random.choice(rows)
        self.weapons.setName(random_row[0])
        self.weapons.setLink(random_row[1])
        conn.close()

    def choose_all(self):
        self.choose_class()
        self.choose_armor()
        self.choose_weapons()
        self.choose_ash_of_war()
        self.choose_shield()
        self.choose_spirit_ash()
        if("S" in self.build_flags or "I" in self.build_flags):
            self.choose_spells()