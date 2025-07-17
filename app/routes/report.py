from flask import Blueprint, render_template, request, send_file, flash
from flask_login import login_required, current_user
from app.models.inscricao import Inscricao
from app.utils.exportador import gerar_csv, gerar_pdf, gerar_xlsx
from io import BytesIO
from datetime import datetime

report_bp = Blueprint('report', __name__, url_prefix='/relatorios')


@report_bp.route('/')
@login_required
def relatorios():
    return render_template('relatorios/index.html')


@report_bp.route('/gerar', methods=['POST'])
@login_required
def gerar_relatorio():
    formato = request.form.get('formato')
    inicio = request.form.get('inicio')
    fim = request.form.get('fim')

    try:
        data_inicio = datetime.strptime(inicio, '%Y-%m-%d')
        data_fim = datetime.strptime(fim, '%Y-%m-%d')
    except:
        flash('Datas inválidas.', 'danger')
        return render_template('relatorios/index.html')

    inscricoes = Inscricao.query.filter(
        Inscricao.data.between(data_inicio, data_fim)
    ).all()

    if not inscricoes:
        flash('Nenhuma inscrição encontrada no período selecionado.', 'info')
        return render_template('relatorios/index.html')

    if formato == 'csv':
        file_data = gerar_csv(inscricoes)
        filename = f"relatorio_{inicio}_a_{fim}.csv"
        mimetype = 'text/csv'
    elif formato == 'xlsx':
        file_data = gerar_xlsx(inscricoes)
        filename = f"relatorio_{inicio}_a_{fim}.xlsx"
        mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    elif formato == 'pdf':
        file_data = gerar_pdf(inscricoes)
        filename = f"relatorio_{inicio}_a_{fim}.pdf"
        mimetype = 'application/pdf'
    else:
        flash('Formato não suportado.', 'danger')
        return render_template('relatorios/index.html')

    return send_file(
        BytesIO(file_data),
        as_attachment=True,
        download_name=filename,
        mimetype=mimetype
    )
