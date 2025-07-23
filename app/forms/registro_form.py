from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistroForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[
        DataRequired(message="Informe seu nome."),
        Length(min=3, max=100, message="Nome deve ter entre 3 e 100 caracteres.")
    ])

    email = StringField('E-mail', validators=[
        DataRequired(message="Informe seu e-mail."),
        Email(message="E-mail inválido.")
    ])

    senha = PasswordField('Senha', validators=[
        DataRequired(message="Crie uma senha."),
        Length(min=4, message="A senha deve ter no mínimo 4 caracteres.")
    ])

    confirmar_senha = PasswordField('Confirmar Senha', validators=[
        DataRequired(message="Confirme sua senha."),
        EqualTo('senha', message="As senhas devem coincidir.")
    ])

    tipo = SelectField('Tipo de Usuário', choices=[
        ('aluno', 'Aluno'),
        ('admin', 'Administrador'),
        ('intermediario', 'Intermediário')
    ], validators=[DataRequired(message="Selecione o tipo de usuário.")])

    submit = SubmitField('Registrar')
