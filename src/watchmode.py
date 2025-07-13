import os
from dotenv import load_dotenv

import urllib.request
import json

from datetime import datetime, timedelta

class Watchmode:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')

    def release_list_append(self, item, releases):
        if item["source_release_date"] == f"{datetime.today().date()- timedelta(days=1)}":
            description = self.request_release_description(item["id"])

            if item["poster_url"] == "":
                releases.append(Release(item["title"], item["type"], description, item["season_number"], 'https://www.reelviews.net/resources/img/default_poster.jpg', item["source_release_date"], item["source_name"]))
            else:
                releases.append(Release(item["title"], item["type"], description, item["season_number"], item["poster_url"], item["source_release_date"], item["source_name"]))

    def request_release_description(self, title_id):
        url = f'https://api.watchmode.com/v1/title/{title_id}/details/?apiKey={self.api_key}'

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data["plot_overview"]

    def request_new_releases(self):
        url = f'https://api.watchmode.com/v1/releases/?apiKey={self.api_key}'

        movie_releases = []
        tv_releases = []

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

            for item in data["releases"]:
                if "movie" in item["type"]:
                    self.release_list_append(item, movie_releases)
                else:
                    self.release_list_append(item, tv_releases)
        
        return movie_releases, tv_releases

class Release:
    def __init__(self, title, type, description, season_number, poster_url, source_release_date, source_name):
        self.title = title
        self.type = type
        self.description = description
        self.season_number = season_number
        self.poster_url = poster_url
        self.source_release_date = source_release_date
        self.source_name = source_name

