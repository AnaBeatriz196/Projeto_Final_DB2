import csv
import io
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

# === CSV ===
def gerar_csv(inscricoes):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Nome do Aluno', 'Data da Refeição', 'Horário de Inscrição', 'Compareceu'])

    for i in inscricoes:
        writer.writerow([
            i.aluno.nome,
            i.refeicao.data.strftime('%d/%m/%Y'),
            i.horario_inscricao.strftime('%H:%M:%S'),
            'Sim' if i.compareceu else 'Não' if i.compareceu is not None else 'Não informado'
        ])

    return output.getvalue().encode('utf-8')


# === XLSX ===
def gerar_xlsx(inscricoes):
    data = []

    for i in inscricoes:
        data.append({
            'Nome do Aluno': i.aluno.nome,
            'Data da Refeição': i.refeicao.data.strftime('%d/%m/%Y'),
            'Horário de Inscrição': i.horario_inscricao.strftime('%H:%M:%S'),
            'Compareceu': 'Sim' if i.compareceu else 'Não' if i.compareceu is not None else 'Não informado'
        })

    df = pd.DataFrame(data)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Relatório')
