import os
from flask import Flask, render_template, redirect, url_for
from . import player

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(SECRET_KEY="dev", DATABASE="../database/db/items.db")

try:
    os.makedirs(app.instance_path)
except OSError:
    pass


@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")


@app.route("/randomize", methods=["POST"])
def display():
    p1 = player.Player()
    p1.choose_all()
    return render_template(
        "index.html",
        starting_class=p1.starting_class.name,
        class_link=p1.starting_class.link,
        helm=p1.helmet.name,
        chest=p1.chest_armor.name,
        gauntlets=p1.gauntlets.name,
        legs=p1.leg_armor.name,
        helm_link=p1.helmet.link,
        chest_link=p1.chest_armor.link,
        gauntlets_link=p1.gauntlets.link,
        legs_link=p1.leg_armor.link,
        weapon=p1.weapons.name,
        weapon_link=p1.weapons.link,
        ash_of_war=p1.ash_of_war.name,
        shield=p1.shield.name,
        spirit_ash=p1.spirit_ash.name,
        ash_of_war_link=p1.ash_of_war.link,
        shield_link=p1.shield.link,
        spirit_ash_link=p1.spirit_ash.link,
    )
