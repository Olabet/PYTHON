
import os
import smtplib
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

username = os.environ.get('email')
password = os.environ.get('password')

msg=MIMEMultipart()
msg['From']='oladejibetty@gmail.com'
msg['To']='ajiloredaniel58@gmail.com'
msg['Subject']='simple email in python'
message='greetings'
msg.attach(MIMEText(message))

mailserver=smtplib.SMTP('smtp.gmail.com',587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('oladejibetty@gmail.com','vubjqlucbagywliu')

mailserver.sendmail('oladejibetty@gmail.com','ajiloredaniel58@gmail.com',msg.as_string())

mailserver.quit()
