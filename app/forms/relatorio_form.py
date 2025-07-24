from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, SubmitField
from wtforms.validators import DataRequired
from datetime import date

class RelatorioForm(FlaskForm):
    inicio = DateField(
        'Data de Início',
        format='%Y-%m-%d',
        default=date.today().replace(day=1),
        validators=[DataRequired(message="Informe a data inicial.")]
    )

    fim = DateField(
        'Data de Fim',
        format='%Y-%m-%d',
        default=date.today,
        validators=[DataRequired(message="Informe a data final.")]
    )

    formato = SelectField(
        'Formato',
        choices=[
            ('pdf', 'PDF'),
            ('xlsx', 'Excel (.xlsx)'),
            ('csv', 'CSV')
        ],
        validators=[DataRequired(message="Selecione um formato.")]
    )

    submit = SubmitField('Gerar Relatório')

    def validate(self, **kwargs):
        valid = super().validate(**kwargs)
        if not valid:
            return False

        if self.inicio.data and self.fim.data and self.inicio.data > self.fim.data:
            self.fim.errors.append('A data final deve ser maior ou igual à data inicial.')
            return False

        return True
