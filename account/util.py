# generate four digit random number
import random


def generate_random_number():
    return random.randint(1000, 9999)


# send email
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


def send_email(receiver, content):
    sender = ''
    password = ''
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr(["Karen", sender])
    msg['To'] = formataddr(["Karen", receiver])
    msg['Subject'] = Header('Your verification code', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
