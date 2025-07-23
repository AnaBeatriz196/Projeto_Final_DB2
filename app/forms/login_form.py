from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[
        DataRequired(message="Informe seu e-mail."),
        Email(message="E-mail inválido.")
    ])

    senha = PasswordField('Senha', validators=[
        DataRequired(message="Informe sua senha."),
        Length(min=4, message="A senha deve ter pelo menos 4 caracteres.")
    ])

    lembrar = BooleanField('Lembrar-me')

    submit = SubmitField('Entrar')
