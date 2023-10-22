from smtplib import *
from email.message import  EmailMessage
import imghdr
import os

#sender and receiver information
sender_email = os.environ.get("EMAIL")
email_password = os.environ.get("PASSWORD")  #go to applicaion password in google and generate one. note: it is not your regular email password
receiver_email = "melvinmc720@yahoo.com"

#message
msg = EmailMessage()
msg["Subject"] = "your desire Subject"
msg["From"] = sender_email
msg["To"] = receiver_email
msg.set_content("you can write your message here")

#attach an image
with open("image.jpg" , "rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
    msg.add_attachment(file_data , maintype="image" , subtype = file_type , filename= file_name)


#attach a pdf file
with open("file.pdf" , "rb") as f:
    file_data = f.read()
    file_name = f.name
    msg.add_attachment(file_data , maintype = "application" , subtype="octet-stream" , filename= file_name)


#add html text
msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head> 
</head>
<body>
<h1> Hello guys , I am melvinmc720 </h1>
</body>
</html>
""" , subtype="html")

#way 1
with SMTP("smtp.gmail.com" , 578) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender_email , email_password)
    smtp.send_message(msg)

#way 2
with SMTP_SSL("smtp.gmail.com" , 465) as smtp:
    smtp.login(sender_email , email_password)
    smtp.send_message(msg)

