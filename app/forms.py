from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

class UserForm(Form):
    name = StringField('name')
    email = StringField('name')

class VendorForm(Form):
    name = StringField('vendor-name')
    component = StringField('component')

class EventForm(Form): 
    name = StringField('component-name')
