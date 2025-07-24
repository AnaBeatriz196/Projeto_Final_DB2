from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.forms.refeicao_form import RefeicaoForm
from app.models.meal import Refeicao
from app.models.user import User
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


def admin_required(func):
    """Decorator para verificar se o usuário logado é administrador."""
    from functools import wraps
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or current_user.tipo != 'admin':
            flash('Acesso restrito a administradores.', 'danger')
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return decorated_view


@admin_bp.route('/painel')
@login_required
@admin_required
def painel():
    return render_template('admin/dashboard_admin.html')


@admin_bp.route('/refeicoes', methods=['GET', 'POST'])
@login_required
@admin_required
def gerenciar_refeicoes():
    form = RefeicaoForm()
    if form.validate_on_submit():
        nova_refeicao = Refeicao(
            data=form.data.data,
            quantidade_vagas=form.quantidade_vagas.data
        )
        db.session.add(nova_refeicao)
        db.session.commit()
        flash('Refeição cadastrada com sucesso!', 'success')
        return redirect(url_for('admin.gerenciar_refeicoes'))

    refeicoes = Refeicao.query.order_by(Refeicao.data.desc()).all()
    return render_template('admin/refeicoes.html', form=form, refeicoes=refeicoes)


@admin_bp.route('/alunos')
@login_required
@admin_required
def listar_alunos():
    alunos = User.query.filter_by(tipo='aluno').all()
    return render_template('admin/alunos.html', alunos=alunos)
