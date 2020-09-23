from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class contactForm(FlaskForm):
    
    correo = StringField('Email', validators=[DataRequired(),Email()]) 
    message = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField("Enviar")


    # DataRequired es para que no dejen el espacio en blanco



