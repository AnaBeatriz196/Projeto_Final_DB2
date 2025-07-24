from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class RefeicaoForm(FlaskForm):
    data = DateField('Data da Refeição', format='%Y-%m-%d', validators=[
        DataRequired(message="Informe a data.")
    ])

    quantidade_vagas = IntegerField('Quantidade de Vagas', validators=[
        DataRequired(message="Informe a quantidade de vagas."),
        NumberRange(min=1, message="Deve haver pelo menos 1 vaga.")
    ])

    submit = SubmitField('Salvar')
