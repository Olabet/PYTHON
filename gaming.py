
import email
import smtplib
import ssl

from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject="An email with attachment from python"
body="This is an email with attachment sent from python"
sender_email="oladejibetty@gmail.com"
receiver_email="oladejiclare@gmail.com"
password=input("vubjqlucbagywliu")

message=MIMEMultipart()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]=subject
message["Bcc"]=receiver_email

message.attach(MIMEText(body,"plain"))

filename="document.pdf"

part=MIMEBase("application","octet-stream")
part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add.header("content-Disposition",
f"attachment;filename={filename}",
)

message.attach(part)
text=message.as_string()

context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,
receiver_email, text)
