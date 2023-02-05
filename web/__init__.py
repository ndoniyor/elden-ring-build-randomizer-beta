import os
from flask import Flask, render_template, redirect, url_for
from . import player

app = Flask(__name__,instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE='../database/db/items.db'
)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route('/', methods=["GET"])
def home_page():
    return render_template('index.html')

@app.route("/randomize", methods=["POST"])
def display():
    p1 = player.Player()
    p1.choose_all()
    return render_template('index.html', 
    starting_class=p1.starting_class[0], class_link=p1.starting_class[1],
    helm=p1.helmet[0], chest=p1.chest_armor[0], gauntlets=p1.gauntlets[0], legs=p1.leg_armor[0], 
    helm_link=p1.helmet[1],chest_link=p1.chest_armor[1],gauntlets_link=p1.gauntlets[1],legs_link=p1.leg_armor[1],
    weapon=p1.weapons[0], weapon_link=p1.weapons[1],
    ash_of_war=p1.ash_of_war[0], shield=p1.shield[0], spirit_ash=p1.spirit_ash[0],
    ash_of_war_link=p1.ash_of_war[1],shield_link=p1.shield[1],spirit_ash_link=p1.spirit_ash[1])