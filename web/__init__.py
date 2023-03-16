import os
from flask import Flask, render_template, redirect, url_for, request

from . import player
from random import choice
import sys

MELEE = 0
SORCERIES = 1
INCANTATIONS = 2
DUAL_WIELD = 3
POWERSTANCE = 4
SINGLE_WIELD = 5
SHIELD = 6

app = Flask(__name__, instance_relative_config=True)
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
    print("form: ",request.form)
    if "armor_sets" in request.form:
        p1.build_flags.append("armor_sets")
    if "melee_sub_flag" in request.form:
        p1.build_flags.append(request.form["melee_sub_flag"])
    if "build_flags" in request.form and "pure_random" not in request.form:
        p1.build_flags.append(int(request.form['build_flags']))
    else:
        p1.build_flags.append(choice([SORCERIES,MELEE,INCANTATIONS]))
    p1.choose_all()

    return render_template(
        "index.html",
        player_info=p1,
        checked_armor=True if "armor_sets" in request.form else False,
        checked_pure=True if "pure_random" in request.form else False,
        checked_melee=True if "build_flags" in request.form else False,
    )
