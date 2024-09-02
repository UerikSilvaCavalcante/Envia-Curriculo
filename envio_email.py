import smtplib
import email.message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def enviar_email(mail, Assunto, vaga):
    try:
        corpo_email = f"""
        <p>Olá, tudo bem?<br>
            Sou o Uerik Saldanha, e estou me candidatando para a vaga de {vaga}.<br>
            Deixei em anexo meu material. Fico no aguardo de um contato para me apresentar melhor. <br>
            Atenciosamente, Uerik Saldanha.</p>
        """

        msg = MIMEMultipart()
        msg['Subject'] = Assunto
        msg['From'] = "uerisalcaval003@gmail.com"
        msg['To'] = mail
        password = "lgsp gimo ubwv xigc"

        msg.attach(MIMEText(corpo_email, 'html'))

        # Anexando arquivo
        filename = 'Curriculo Profissional Uerik Saldanha.pdf'  # Substitua pelo nome do arquivo que deseja anexar
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        s.quit()
        return 'Email enviado'
    except :
        return 'Erro ao enviar email'
    # print('Email Enviado')

# mail = str(input('Email: '))
# assunto = str(input('Assunto: '))
# vaga = str(input('Vaga: '))
# enviar_email(mail,assunto, vaga)