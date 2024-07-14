import requests
from dotenv import load_dotenv
import os, json, time

from gpio import turn_on_red, turn_on_green, turn_off_green, turn_off_red

load_dotenv()  # take environment variables from .env.

url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/K04"

payload = {}
headers = {
  'api_key': os.environ['WMATA_API_KEY']
}

response = requests.request("GET", url, headers=headers, data=payload)

print(json.dumps(response.json(), indent=2))

trains = response.json()["Trains"]
data = []
for i in trains:
    if i["Destination"] == "Vienna":
        data.append(int(i["Min"]))
    
data.sort()
print(data)
if len(data) > 0 and data[0] < 5:
    turn_on_red()
else:
    turn_on_green()

time.sleep(5)
turn_off_green()
turn_off_red()