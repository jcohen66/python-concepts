import smtplib
import imapclient as imap
from dotenv import load_dotenv
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

load_dotenv('.env')
username: str = os.getenv('USERNAME')
password: str = os.getenv('PASSWORD')


# server = smtplib.SMTP('smtp.gmail.com', 25)
server = imap.IMAPClient('imap.gmail.com', ssl=True)
server.login(username, password)

# Add header
msg = MIMEMultipart()
msg['From'] = 'NeuralNine'
msg['To'] = 'jcohen66@live.com'
msg['Subject'] = 'Kangaroos'

# Add text
with open('message.txt', 'r') as f:
    message = f.read()
msg.attach(MIMEText(message, "plain")) 

# Attach image file
filename = 'test_image.jpg'
attachment = open(filename, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('content-disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string
server.sendmail('jcohen66g@gmail.com', to='jcohen66@live.com')
