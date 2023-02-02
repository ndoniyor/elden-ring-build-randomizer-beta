from flask_wtf import FlaskForm
from wtforms import SubmitField

class Button(FlaskForm):
    submit = SubmitField('Randomize')