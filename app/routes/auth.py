from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms.login_form import LoginForm
from app.forms.registro_form import RegistroForm
from app.models.user import User
from app import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.senha.data):
            login_user(user, remember=form.lembrar.data)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Credenciais inválidas.', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da conta.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        user = User(nome=form.nome.data, email=form.email.data, tipo=form.tipo.data)
        user.set_password(form.senha.data)
        db.session.add(user)
        db.session.commit()
        flash('Conta criada com sucesso! Faça login.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('registro.html', form=form)
