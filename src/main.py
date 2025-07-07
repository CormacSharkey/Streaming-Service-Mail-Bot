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
<div style="display: table;">
<div style="display: table-row;">
"""

column = 0

for item in releases:
    if column == 7:
        column = 0
        html += """\
        </div>
        <div style="display: table-row;">
        """

    html += f"""\
    <div style="width: 205px; display: table-cell;">
    <img src={item.poster_url} width=200px style="border: 3px solid black;" alt="Poster Image">
    <p style="border: 3px solid black;">
    Title: {item.title}<br>
    Type: {item.type}<br>
    Season Number: {item.season_number}<br>
    Release Date: {item.source_release_date}<br>
    Platform: {item.source_name}
    </p>
    </div>

    <div style="width: 10px; display: table-cell;"></div>

    """
    column += 1

html += """\
</div>
</div>
</body>
</html>
"""

smtp = Smtp(os.getenv('APP_PASSWORD'), os.getenv('SENDER_EMAIL'), os.getenv('RECEIVER_EMAIL'))

smtp.send_mail("smtp testing - borders", html)

# print(html)