import smtplib

# create an SMTP object
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS encryption
smtp_obj.starttls()

# login to the email account
smtp_obj.login('codelessearnmore@gmail.com', 'YOUR_PASSWORD')

# construct the email message
message = "Subject: Email sent by ChatGPT\n\nChatGPT rocks!"

# send the email
smtp_obj.sendmail('codelessearnmore@gmail.com', 'frank@codelessearnmore.com', message)

# close the SMTP connection
smtp_obj.quit()