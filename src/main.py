import os
from dotenv import load_dotenv

from datetime import datetime

from watchmode import Watchmode
from smtp import Smtp
from utils import type_map, type_check

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
    if item.source_release_date == f"{datetime.today().date()}":
        if column == 5:
            column = 0
            html += """\
            </div>
            <div style="display: table;">
            """

        html += f"""\
        <div style="display: table-cell;">
        <center>
        <img src={item.poster_url} height={cell_height}px style="border: 3px solid black;" alt="Poster Image">
        <p style="background-color:powderblue; border: 3px solid black;">
        <b>{item.title}</b><br>
        Type: {type_map(item.type)}<br>
        Season Number: {item.season_number}<br>
        Release Date: {item.source_release_date}<br>
        Platform: {item.source_name}
        </p>
        </center>
        </div>

        """
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

print(html)