import os
import requests

api_key = os.environ.get("USDA_API_KEY")

headers = {
    'X-Api-Key': api_key
}

response = requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1', headers=headers)

print(response.status_code)