import os
from dotenv import load_dotenv

import urllib.request
import json

class Watchmode:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')

    def request_new_releases(self):
        url = f'https://api.watchmode.com/v1/releases/?apiKey={self.api_key}'

        releases = []

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

            for item in data["releases"]:
                if item["poster_url"] == "":
                    releases.append(Release(item["title"], item["type"], item["season_number"], 'https://www.reelviews.net/resources/img/default_poster.jpg', item["source_release_date"], item["source_name"]))
                else:
                    releases.append(Release(item["title"], item["type"], item["season_number"], item["poster_url"], item["source_release_date"], item["source_name"]))
        
        return releases

class Release:
    def __init__(self, title, type, season_number, poster_url, source_release_date, source_name):
        self.title = title
        self.type = type
        self.season_number = season_number
        self.poster_url = poster_url
        self.source_release_date = source_release_date
        self.source_name = source_name
