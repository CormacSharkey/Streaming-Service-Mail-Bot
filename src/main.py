import os
from dotenv import load_dotenv

load_dotenv()

watchmode_api_key = os.getenv('API_KEY')

# print(watchmode_api_key)


import urllib.request
import json

url = f'https://api.watchmode.com/v1/releases/?apiKey={watchmode_api_key}'

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

    for item in data["releases"]:
        print(item["title"], item["source_name"])