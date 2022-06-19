#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                          Email Sender                                         # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Send an html e-mail from a Python script using Google Gmail.                          #
#                                                                                       #
# Requirements:                                                                         #
# Google Gmail Account                                                                  #
# Enable 2-Step Verification on your Gmail Account (required to get an App Password)    #
# Gmail App Password (lets you sign in with apps like Python scripts)                   #
# Gmail app password setup: https://myaccount.google.com/apppasswords                   #
# documentation: https://support.google.com/accounts/answer/185833                      #
#                                                                                       #
# Guide:                                                                                #
# 1. Review/edit the Index.html message file being sent.                                #
# 2. Review/edit the name, greeting, number substitutes below.                          #
# 3. Update the Send To Email Address below.                                            #
# 4. Update your Gmail address and Gmail app password below.                            #
# 5. Launch by clicking run button in top right in VSCode or: py -3 send_email.py       #
#########################################################################################

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Anthony'
# Send To Email Address (use another email to test)
email['to'] = 'yourotheremail@yahoo.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(
    # these fields
    {'name': 'John', 'greeting': 'Hello friend!', 'number': "867-5309"}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Your Gmail address and Gmail app password
    smtp.login('youremail@gmail.com', 'gmailapppassword')
    smtp.send_message(email)
    print('Message Successfully Sent')
