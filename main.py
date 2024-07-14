import requests
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/K04"

payload = {}
headers = {
  'api_key': os.environ['WMATA_API_KEY']
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
