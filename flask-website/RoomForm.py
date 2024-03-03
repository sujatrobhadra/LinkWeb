from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms import validators
class RoomForm(Form):
    text=StringField('Room Name:', validators=[validators.input_required()])
    submitted=SubmitField('SUbmit')


