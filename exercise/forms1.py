from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPet(FlaskForm):
    """form to add pets"""
    name = StringField('Pet Name', validators = [InputRequired()])
    species = SelectField('Species', choices = [('cat', 'Cat'),
    ('dog', 'Dog'), ('pig', 'Pig'), ('porcupine', 'Porcupine')])
    #question asked for dog, cat, porcupine,
    photo_url = StringField('Photo URL', validators = [Optional(),
    URL()])

    age = IntegerField('Age', validators = [Optional(),
    NumberRange(min = 0, max = 30)])
    #since step 5 asked to put the age between 0 and 30, we can
    notes = StringField('Notes', validators = [Optional()])

class EditPet(FlaskForm):
    """Form to edit a pet"""
    photo_url = StringField('Photo URL', validators = [Optional(),
    URL()])

    notes = StringField('Notes', validators=[Optional()
    ])

    available = BooleanField('Available?')

    
