import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("oladejibetty@gmail.com","vubjqlucbagywliu")
server.sendmail("oladejibetty@gmail.com",
                "oladejiclare@gmail.com",
                "i just sent you a message using python")

server.quit()               
                



           