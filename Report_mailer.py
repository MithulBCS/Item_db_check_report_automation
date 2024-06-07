import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



# server and user credentials
SMTP_SERVER = "smtp"   # search for microsoft 365, outlook.com
PORT = ""    # TLS = 587, SSL = 465
SMTP_USER = ""  # BCS mail
SMTP_PASSWORD = ""   # Password


# List of the recipients
recipients = []


# email content
subject = "Discrepancy Report date--"

html_content = """

<html>


"""


# function to send email
def send_mail(to_address, subject, html_content):
    msg = MIMEMultipart("alternative")
    msg["From"] = SMTP_USER
    msg["To"] = to_address
    msg["Subject"] = subject

    part = MIMEText(html_content, "html")
    msg.attach(part)


    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        server.starttls()  # secure the connection
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, to_address, msg.as_string())
        print(f"Email sent to {to_address}")



# Send email to each recipient
for recipient in recipients:
    send_mail(recipient, subject, html_content)
