import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Configurações de e-mail (pode ser carregado via .env)
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USER = os.getenv('EMAIL_USER', 'seu-email@ifome.com')
EMAIL_PASS = os.getenv('EMAIL_PASS', 'sua-senha')

def enviar_email(destinatario, assunto, corpo_html):
    """Envia um e-mail HTML para o destinatário informado."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = destinatario
        msg['Subject'] = assunto

        msg.attach(MIMEText(corpo_html, 'html'))

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

        print(f"E-mail enviado para {destinatario}")
        return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False


# Exemplo de uso:
def notificar_confirmacao_inscricao(aluno):
    assunto = "IFome - Confirmação de Inscrição"
    corpo = f"""
    <h3>Olá, {aluno.nome}!</h3>
    <p>Sua inscrição para a refeição do dia foi registrada com sucesso.</p>
    <p>Por favor, compareça ao restaurante no horário adequado.</p>
    <p><strong>IFome - Sistema de Alimentação do IFPB</strong></p>
    """
    return enviar_email(aluno.email, assunto, corpo)
