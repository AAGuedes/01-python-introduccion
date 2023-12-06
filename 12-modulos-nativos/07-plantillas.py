# Habilitar envio de correos por SMTP para GMAIL
# https://myaccount.google.com/u/1/lesssecureapps
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib


# Plantilla HTML
plantilla = Path("12-modulos-nativos/plantilla.html").read_text(encoding="UTF-8")
template = Template(plantilla)
cuerpo = template.substitute({"usuario": "John Doe"})
cuerpo = template.substitute(usuario="John Doe")

# Adjunatr una imágen al mensaje
path = Path("12-modulos/imagen.png")
mime_image = MIMEImage(path.read_bytes())

# Construcción del mensaje
mensaje = MIMEMultipart()
mensaje["from"] = "John Doe"
mensaje["to"] = "destiny@gmail.com"
mensaje["subject"] = "Mail de prueba"
cuerpo = MIMEText(cuerpo, "html")

mensaje.attach(cuerpo)
mensaje.attach(mime_image)

# Enviar mensaje
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("username@gmail.com", "password")
    smtp.send_message(mensaje)
    print("Mensaje enviado")
