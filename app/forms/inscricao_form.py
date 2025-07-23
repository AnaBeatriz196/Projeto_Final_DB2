from flask_wtf import FlaskForm
from wtforms import DateTimeField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

class InscricaoForm(FlaskForm):
    horario_inscricao = DateTimeField('Horário da Inscrição', default=datetime.utcnow, validators=[
        DataRequired(message="Horário obrigatório.")
    ])

    submit = SubmitField('Confirmar Inscrição')
