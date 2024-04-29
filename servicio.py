import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configura los detalles del servidor SMTP 
smtp_server = 'smtp.gmail.com'
smtp_puerto = 587

# Función principal
def enviar_correo(username, password, destinatario, asunto, mensaje, archivo, extension):
    smtp_username = username
    smtp_password = password 
    
    # Crea un objeto MIME multipart
    msg = MIMEMultipart()

    # Agrega el contenido de texto
    msg.attach(MIMEText(mensaje, 'plain'))

    # Agrega un archivo adjunto
    with open(archivo, 'rb') as file:
        adjunto = MIMEBase('application', 'octet-stream')
        adjunto.set_payload(file.read())
        encoders.encode_base64(adjunto)
        adjunto.add_header('Content-Disposition', f'attachment; filename="{archivo}"')
        adjunto.add_header('Content-Type', extension)
        msg.attach(adjunto)

    # Inicia una conexión con el servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_puerto)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.set_debuglevel(1)
    print("Conexion exitosa")

    # Envía el correo electrónico
    msg['From'] = smtp_username
    msg['To'] = destinatario
    msg['Subject'] = asunto

    server.sendmail(smtp_username, destinatario, msg.as_string())
    print("Mensaje enviado")

    # Cierra la conexión con el servidor SMTP
    server.quit()
