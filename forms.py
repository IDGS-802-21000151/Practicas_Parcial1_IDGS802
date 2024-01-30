from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms import EmailField
from wtforms import validators

class distanciaFormulario(Form):
    x1 = StringField("x1")
    y1 = StringField("y1")
    x2 = StringField("x2")
    y2 = StringField("y2")