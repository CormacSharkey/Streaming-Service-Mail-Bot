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
<div style="border: 8px solid red; display: table;">
"""

column = 0

cell_width = "230"

for item in releases:
    if column == 6:
        column = 0
        html += """\
        </div>
        <div style="border: 8px solid red; display: table;">
        """

    html += f"""\
    <div style="width: 245px; display: table-cell;">
    <center>
    <img src={item.poster_url} width={cell_width}px style="border: 3px solid black;" alt="Poster Image">
    <p style="width: {cell_width}px; border: 3px solid black;">
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

# print(html)