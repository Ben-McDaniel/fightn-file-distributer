import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = 'Hello, his is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP libraryThank You '
#The mail addresses and password
sender_address = 'XXXXXXXXXXxx@gmail.com'
sender_pass = 'XXXXXXXXXXX'
receiver_address = 'mcdanbj2@jhuapl.edu'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')