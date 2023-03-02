import random
import sqlite3 as sql
import sys

DATABASE_DIR = "database/db/items.db"
SELECTION_STR = "SELECT * FROM "

MELEE = 0
SORCERIES = 1
INCANTATIONS = 2
DUAL_WIELD = 3
POWERSTANCE = 4
SINGLE_WIELD = 5
SHIELD = 6


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
        self.starting_class = Item(name="")
        self.build_flags = []
        self.helmet = Item(name="")
        self.chest_armor = Item(name="")
        self.gauntlets = Item(name="")
        self.leg_armor = Item(name="")
        self.ash_of_war = []
        self.spells = []
        self.weapons = []
        self.spirit_ash = Item(name="")

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

    def choose_ash_of_war(self, weapon_types):
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        for weapon_type in weapon_types:
            cursor.execute(SELECTION_STR + 'ashes WHERE type LIKE "%' + weapon_type + '%"')
            rows = cursor.fetchall()
            print("type= ",weapon_type)
            random_row = random.choice(rows)
            self.ash_of_war.append(Item(random_row[0],random_row[1]))
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
        if SORCERIES in self.build_flags:
            cursor.execute(SELECTION_STR + "sorceries ORDER BY RANDOM() LIMIT 5")
            rows = cursor.fetchall()
        elif INCANTATIONS in self.build_flags:
            cursor.execute(SELECTION_STR + "incantations ORDER BY RANDOM() LIMIT 5")
            rows = cursor.fetchall()
        for spell in rows:
            self.spells.append(Item(spell[0],spell[1]))
        conn.close()


    def choose_weapons(self):
        weapon_metadata = []
        conn = sql.connect(DATABASE_DIR)
        cursor = conn.cursor()

        cursor.execute(SELECTION_STR + "weapons")
        rows = cursor.fetchall()

        first_wep = random.choice(rows)
        self.weapons.append(Item(first_wep[0],first_wep[1]))

        if POWERSTANCE in self.build_flags:
            cursor.execute(SELECTION_STR + 'weapons WHERE type="' + first_wep[3] + '"')
            rows = cursor.fetchall()

            second_wep = random.choice(rows)
            self.weapons.append(Item(second_wep[0],second_wep[1]))

        elif DUAL_WIELD in self.build_flags:
            cursor.execute(SELECTION_STR + "weapons")
            rows = cursor.fetchall()

            second_wep = random.choice(rows)
            self.weapons.append(Item(second_wep[0],second_wep[1]))
        elif SHIELD in self.build_flags:
            cursor.execute(SELECTION_STR + "shields")
            rows = cursor.fetchall()

            second_wep = random.choice(rows)
            self.weapons.append(Item(second_wep[0],second_wep[1]))


        conn.close()
        if(first_wep[2] is not 'n'):
            weapon_metadata.append(first_wep[3])
        try: 
            if(second_wep[2] is not 'n'):
                weapon_metadata.append(second_wep[3])
        except UnboundLocalError:
            pass

        return weapon_metadata

    def choose_all(self):
        if(MELEE in self.build_flags):
            self.build_flags.append(random.choice([POWERSTANCE, DUAL_WIELD, SINGLE_WIELD, SHIELD]))
        self.choose_class()
        self.choose_armor()
        weapon_types = self.choose_weapons()

        
        if(weapon_types):
            self.choose_ash_of_war(weapon_types)
            print(*self.ash_of_war)
        self.choose_spirit_ash()
        if(SORCERIES in self.build_flags or INCANTATIONS in self.build_flags):
            self.choose_spells()