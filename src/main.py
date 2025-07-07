import os
from dotenv import load_dotenv

from watchmode import Watchmode
from smtp import Smtp

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

watchmode = Watchmode()

releases = watchmode.request_new_releases()

html = """\
<html>
<body>
"""

for item in releases:
    html += f"""\
    <div>
    <img src={item.poster_url} alt="Poster Image">
    <p>
    {item.title}<br>
    {item.type}<br>
    {item.season_number}<br>
    {item.source_release_date}<br>
    {item.source_name}
    </p>
    </div>
    """

html += """\
</body>
</html>
"""

smtp = Smtp(os.getenv('APP_PASSWORD'), os.getenv('SENDER_EMAIL'), os.getenv('RECEIVER_EMAIL'))

smtp.send_mail("smtp panel testing", html)

# print(html)