from wtforms import Form
from wtforms import StringField, SelectField, RadioField
from wtforms.validators import DataRequired

class distanciaFormulario(Form):
    x1 = StringField("x1")
    y1 = StringField("y1")
    x2 = StringField("x2")
    y2 = StringField("y2")

class ResistenciaFormulario(Form):
    opcionesBandasDeColor = [("0", "Negro - 0"), ("1", "Café - 1"), ("2", "Rojo - 2"), ("3", "Naranja - 3"), ("4", "Amarillo - 4"), ("5", "Verde - 5"), ("6", "Azul - 6"), ("7", "Morado - 7"), ("8", "Gris - 8"), ("9", "Blanco - 9")]
    primeraBanda = SelectField("Primera banda de color", choices=opcionesBandasDeColor)
    segundaBanda = SelectField("Segunda banda de color", choices=opcionesBandasDeColor)
    
    opcionesMultiplicador = [("1", "Negro - x1"), ("10", "Café - x10"), ("100", "Rojo - x100"), ("1000", "Naranja - x1000"), ("10000", "Amarillo - x10000"), ("100000", "Verde - x100000"), ("1000000", "Azul - x1000000"), ("10000000", "Violeta - x10000000"), ("100000000", "Gris - x100000000"), ("1000000000", "Blanco - x1000000000")]
    multiplicador = SelectField("Tercera banda de color", choices=opcionesMultiplicador)
    
    tolerancia = RadioField("Selecciona tolerancia", choices=[('5', 'Oro'), ('10', 'Plata')], default='5', validators=[DataRequired()])