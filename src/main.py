import os
from dotenv import load_dotenv

from datetime import datetime, timedelta

from watchmode import Watchmode
from smtp import Smtp
from utils import html_chunk


# TODO:
# Add a description for the item
# Sort movies from tv shows and display them separately in email
# Pretty up the html
# Figure out best way to have the script run constantly to execute every day (aim for time when globally the world is "today")
# Write README

load_dotenv()

watchmode = Watchmode()

releases = watchmode.request_new_releases()

html = """\
<html>
<body>
<center>
<div style="display: table;">
"""

column = 0

cell_height = "400"


for item in releases:
    if item.source_release_date == f"{datetime.today().date()- timedelta(days=1)}":
        if column == 5:
            column = 0
            html += """\
            </div>
            <div style="display: table;">
            """

        html += html_chunk(item, cell_height)
        column += 1

html += """\
</div>
</div>
</center>
</body>
</html>
"""

smtp = Smtp(os.getenv('APP_PASSWORD'), os.getenv('SENDER_EMAIL'), os.getenv('RECEIVER_EMAIL'))

smtp.send_mail(f"html testing {datetime.now()}", html)

# print(html)