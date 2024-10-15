import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações de envio de e-mail
smtp_server = 'smtp.seuprovedor.com'
smtp_port = 587
username = 'seuemail@provedor.com'
password = 'suasenha'

# Função para enviar o e-mail
def enviar_email(destinatario, assunto, corpo):
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adiciona o corpo da mensagem
    msg.attach(MIMEText(corpo, 'plain'))

    # Conecta ao servidor SMTP e envia o e-mail
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, destinatario, msg.as_string())
        server.quit()
        print(f"E-mail enviado para {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar e-mail para {destinatario}: {str(e)}")

# Lê os e-mails do arquivo CSV
with open('emails.csv', newline='') as csvfile:
    leitor_csv = csv.reader(csvfile)
    for linha in leitor_csv:
        email = linha[0]  # O e-mail está na primeira coluna
        # Aqui você pode personalizar a mensagem e o assunto
        assunto = 'Sua newsletter'
        corpo = 'Aqui está o conteúdo da sua newsletter.'
        enviar_email(email, assunto, corpo)