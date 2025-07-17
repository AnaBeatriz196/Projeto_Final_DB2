from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.forms.inscricao_form import InscricaoForm
from app.models.refeicao import Refeicao
from app.models.inscricao import Inscricao
from app import db
from datetime import date

student_bp = Blueprint('student', __name__, url_prefix='/aluno')


@student_bp.route('/painel')
@login_required
def painel_aluno():
    return render_template('aluno/dashboard_aluno.html')


@student_bp.route('/inscrever', methods=['GET', 'POST'])
@login_required
def inscrever():
    form = InscricaoForm()
    hoje = date.today()

    refeicao = Refeicao.query.filter_by(data=hoje).first()
    if not refeicao:
        flash('Nenhuma refeição disponível para hoje.', 'warning')
        return redirect(url_for('student.painel_aluno'))

    if Inscricao.query.filter_by(aluno_id=current_user.id, refeicao_id=refeicao.id).first():
        flash('Você já se inscreveu para a refeição de hoje.', 'info')
        return redirect(url_for('student.painel_aluno'))

    if form.validate_on_submit():
        nova_inscricao = Inscricao(
            aluno_id=current_user.id,
            refeicao_id=refeicao.id,
            horario_inscricao=form.horario_inscricao.data
        )
        db.session.add(nova_inscricao)
        db.session.commit()
        flash('Inscrição realizada com sucesso!', 'success')
        return redirect(url_for('student.painel_aluno'))

    return render_template('aluno/inscricao.html', form=form, refeicao=refeicao)


@student_bp.route('/historico')
@login_required
def historico():
    inscricoes = Inscricao.query.filter_by(aluno_id=current_user.id).order_by(Inscricao.data.desc()).all()
    return render_template('aluno/historico.html', inscricoes=inscricoes)


@student_bp.route('/faltas')
@login_required
def ver_faltas():
    inscricoes = Inscricao.query.filter_by(aluno_id=current_user.id).all()
    faltas = [i for i in inscricoes if i.compareceu is False]
    return render_template('aluno/faltas.html', faltas=faltas, total=len(faltas))
