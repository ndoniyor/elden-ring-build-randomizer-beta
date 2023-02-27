import os
from flask import Flask, render_template, redirect, url_for, request

from . import player
import sys

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
    p1.build_type = "I"
    if "armor_sets" in request.form:
        p1.build_flags.append("armor_sets")
    p1.choose_all()
    print(type(p1.spells), p1.spells[0], p1.spells[0].name, file=sys.stdout)

    return render_template(
        "index.html",
        player_info=p1,
        checked=True if "armor_sets" in request.form else False,
    )
