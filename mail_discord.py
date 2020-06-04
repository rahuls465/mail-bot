#required modules
import os
import smtplib
import imghdr
import re
import argparse
from email.message import EmailMessage
#sender
def mmsend (mail,subject='from bot',message='hello') :
    msg = EmailMessage()
    msg['subject'] = subject
    msg['From'] = os.environ.get('email')
    msg['To'] = mail
    print(os.environ.get('email'),os.environ.get('email_pass'))
    msg.set_content(message)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(os.environ.get('email'),os.environ.get('email_pass'))
        smtp.send_message(msg)
    return('Done')
