import os
from flask import Flask, render_template
from randomize import Button
def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='../database/db/items.db'
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def home_page():
        button = Button()
        return render_template('index.html', button=button)
    return app