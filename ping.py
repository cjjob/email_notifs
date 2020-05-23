#### Simplest version for plaintext email

# import smtplib, ssl

# port = 465  # For SSL
# smtp_server = 'smtp.gmail.com'
# sender_email = 'cjjobdev@gmail.com'  # Enter your address
# receiver_email = 'obriencjj@gmail.com'  # Enter receiver address
# password = 'codepleaseworkthx'
# message = '''
# Hey mate, your spaghetti code finished.

# Best of luck!
# '''

# # Create a secure SSL context
# context = ssl.create_default_context()

# with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
#     server.login('cjjobdev@gmail.com', password)
#     server.sendmail(sender_email, receiver_email, message)


#### If you want to get a little fancy

import configparser
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up config parser
config = configparser.ConfigParser()
config.read('config.ini')

# Read values from the config file
port = config['default'].getint('port')  # For SSL
smtp_server = config['default']['smtp_server']
sender_email = config['user_info']['email']
password = config['user_info']['password']

# Send the email to... 
receiver_email = 'obriencjj@gmail.com'

# Combines HTML and plaintext for two rendering options
message = MIMEMultipart('alternative')
message['Subject'] = 'fancy_email'
message['From'] = sender_email
message['To'] = receiver_email

# Create the plain-text and HTML version of your message
text = '''
Hey mate, your spaghetti code finished.

Best of luck!
'''

html = '''
<html>
  <body>
  	<h3>Yo!</h3>
    <p>
       Code "borrowed" from	\
       <a href='https://realpython.com/python-send-email/'> \
       Real Python </a> 
    </p>
  </body>
</html>
'''

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )