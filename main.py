import os
from dotenv import load_dotenv

load_dotenv()

watchmode_api_key = os.getenv('API_KEY')

print(watchmode_api_key)