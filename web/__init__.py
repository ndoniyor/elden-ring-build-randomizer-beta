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
    starting_class=p1.starting_class, 
    helm=p1.helmet, chest=p1.chest_armor, gauntlets=p1.gauntlets, legs=p1.leg_armor, weapon=p1.weapons,
    ash_of_war=p1.ash_of_war, shield=p1.shield, spirit_ash=p1.spirit_ash)