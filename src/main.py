import os
from dotenv import load_dotenv
from datetime import datetime

from watchmode import Watchmode
from smtp import Smtp
from utils import html_body_chunk


# TODO:
# Write comments
# Write README

# Load the .env
load_dotenv()

# Create a Watchmode obj
watchmode = Watchmode()

# Get the movie and tv releases lists
movie_releases, tv_releases = watchmode.request_new_releases(-1)

# Get the html body from the movie and tv releases
html = html_body_chunk(movie_releases, tv_releases, "400", 5)

# Create an Smtp obj
smtp = Smtp(os.getenv('APP_PASSWORD'), os.getenv(
    'SENDER_EMAIL'), os.getenv('RECEIVER_EMAIL'))

# Send the html body as an email
smtp.send_mail(f"html testing {datetime.now()}", html)
