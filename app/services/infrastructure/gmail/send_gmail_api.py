import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings

# Variables
email_user = settings.EMAIL_USER
email_pass = settings.EMAIL_PASS

email_to = "jefersson.quicana@utec.edu.pe"

subject = "📩 Mensaje automático diario"
body = "Hola! Este es tu correo enviado automáticamente desde Python 💻."

def enviar_correo():
    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = email_to
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email_user, email_pass)
            server.send_message(msg)
            print("✅ Correo enviado exitosamente")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    enviar_correo()
