import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_tiktok_data(region="us", count=10):
    url = "https://tiktok-scraper7.p.rapidapi.com/feed/list"
    querystring = {"region": region, "count": count}
    headers = {
        "X-RapidAPI-Key": os.getenv("X_RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
