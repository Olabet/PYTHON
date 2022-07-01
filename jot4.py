
from email.message import EmailMessage
import smtplib
import os
import ssl
username = os.environ.get('username')
password = os.environ.get('password')


email_sender = 'oladejibetty@gmail.com'
email_password = 'putrfsqtkmfqgrhp'
email_reciever ='booladeji68@student.lautech.edu,ng'

subject ='check out my python email'
body = """
i've just sent you an email with python code 
"""
em = EmailMessage()
em['From'] = Email_sender
em['To'] = Email_receiver
em['Subject'] =Subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)as smtp:
    smtp.login(Email_sender,Email_password)
    smtp.sendmail(Email_sender,Email_receiver, em.as_string())

print("Email sent!")

