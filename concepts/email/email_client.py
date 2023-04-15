# Fetch Email Inbox
# pip install imapclient

import imapclient as imap
import email
from dotenv import load_dotenv
import os

load_dotenv('.env')

# Connect to Email Server
EMAIL_SERVER = os.getenv('EMAIL_SERVER')
ACCOUNT = os.getenv('ACCOUNT')
PASSWORD = os.getenv('PASSWORD')
server = imap.IMAPClient('imap.gmail.com', ssl=True)
server.login(ACCOUNT, PASSWORD)

# Select Inbox
server.select_folder('INBOX')

# Search for unread emails
messages = server.search(['UNSEEN'])

# Fetch Email Body, Subject, From, Date
for uid, msg_data, in server.fetch(messages, 'RFC822').items():
    email_message = msg_data[b'RFC822'].decode('utf-8')
    mail = email.message_from_string(email_message)
    print('From:', mail['From'])
    print('Subject:', mail['Subject'])
    print('Date:', mail['Date'])
    print('Body:', mail.get_payload())
    # Mark as read
    server.set_flags(uid, '\Seen')
    
# close connection
server.logout()
    