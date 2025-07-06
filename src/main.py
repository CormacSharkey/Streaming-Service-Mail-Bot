import os
from dotenv import load_dotenv

from watchmode import Watchmode, Release

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

watchmode = Watchmode()

releases = watchmode.request_new_releases()

html = """\
<body>
<html>
"""

for item in releases:
    html += f"""\
    <p>
    <img src={item.poster_url} alt="Poster Image"><br>
    {item.title}<br>
    {item.type}<br>
    {item.season_number}<br>
    {item.source_release_date}<br>
    {item.source_name}<br>
    </p>
    """




port = 465  # For SSL
password = os.getenv('APP_PASSWORD')

sender_email = os.getenv('SENDER_EMAIL')
receiver_email = os.getenv('RECEIVER_EMAIL')

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email


# Create the plain-text and HTML version of your message
# text = """\
# Hi,
# How are you today?
# Real Python has many great tutorials:
# www.realpython.com"""

# html = f"""\
# <html>
# <body>
#     <p>Hi,<br>
#     How are you today?<br>
#     <a href="http://www.realpython.com">Real Python</a> 
#     has many great tutorials.
#     </p>

#     <img src={image} alt="Italian Trulli">
# </body>
# </html>
# """

# Turn these into plain/html MIMEText objects
# part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
# message.attach(part1)
message.attach(part2)

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())