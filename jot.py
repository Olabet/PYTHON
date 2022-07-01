# new_srt="the cow jumped over the moon"
# print(new_srt.split())
# name='jim'
# student=name
# name='tom'
# print(name)
# print(student)



# my_lst=[1,2,3,4,5]
# my_lst[0]='one'
# print(my_lst)

# mv_popu=74728
# mv_popu+=4000-600
# print(mv_popu)

# if season==spring
#     print('plant the garden:')
# elif season =='summer':
#     print('water the garden:')
# elif season =='fall':
#     print('harvest the garden:')
# elif season =='winter':
#     print('stay indoors:')


# n=4
# if n%2 == 0
# print("number" + str(n) + "is even")
# print(n)









# from email.message import emailmessage
# import smtplib
# import os
# import ssl
# username = os.environ.get('email')
# password = os.environ.get('psw')


# email_sender = 'oladejibetty@gmail.com'
# email_password = 'putrfsqtkmfqgrhp'
# email_reciever ='booladeji68@student.lautech.edu.ng'

# subject ='greetings'
# body = """
# how are you today
# """
# em = emailmessage()
# em['from'] = email_sender
# em['to'] = email_receiver
# em['subject'] = subject
# em.set_content(body)

# context = ssl.create_default_context()

# with smyplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
#     smtp.login(email_sende,email_password)
#     smtp.sendmail(email_sender,email_receiver, em.as_string())

# print('emailsent!')



import smtplib
server=smtplib_SMTP_SSL('smtp.gmail.com',465)
server.login('oladejibetty@gmail.com','putrfsqtkmfqgrhp')
server.sendmail('from oladejibetty@gmail.com',
    'to booladeji68@student.lautech.edu.ng',
    'this message is from python')

server.quit()



