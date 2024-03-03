from flask_wtf import Form
from wtforms.fields import StringField, SelectField, SubmitField
from wtforms import validators
class AddForm(Form):
    idd=StringField('ID', validators=[validators.input_required()])
    content=StringField('Content', validators=[validators.input_required()])
    typed=SelectField('Type',choices=('Link', 'Text', 'Images'))
    group=StringField('Grp',validators=[validators.input_required()])
    submitted=SubmitField('Submit')
