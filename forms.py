from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, ValidationError
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired(), AnyOf(['cat', 'dog', 'fish', 'hamster'])])
    image_link = StringField('Image URL', validators=[URL()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30)])
    available = BooleanField('Available')
    notes = StringField('Notes')


class EditPetForm(FlaskForm):
    """Form for editing pets."""

    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired(), AnyOf(['cat', 'dog', 'fish', 'hamster'])])
    image_link = StringField('Image URL', validators=[URL()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30)])
    available = BooleanField('Available')
    notes = StringField('Notes')
