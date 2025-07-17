from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
import ssl


class Smtp:
    def __init__(self, app_password, sender_email, receiver_email):
        self.port = 465  # Port
        self.app_password = app_password  # App password (gmail)
        self.sender_email = sender_email  # Sender email (gmail)
        self.receiver_email = receiver_email  # Receiver email

    # Send an email with subject line and html body
    def send_mail(self, subject, html):
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        html_part = MIMEText(html, "html")
        message.attach(html_part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.sender_email, self.app_password)
            server.sendmail(self.sender_email,
                            self.receiver_email, message.as_string())
