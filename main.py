import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("USDA_API_KEY")
SEARCH_TERM = "chicken breast"

url = "https://api.nal.usda.gov/fdc/v1/foods/search"
params = {
    "query": SEARCH_TERM,
    "pageSize": 3
}
headers = {
    'X-Api-Key': API_KEY
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Search results for:", SEARCH_TERM)
    for food in data.get("foods", []): # if "foods" missing, return empty list
        print(f"- {food.get('description')} (FDC ID: {food.get('fdcId')})")
else:
    print("Error:", response.status_code, response.text)

# response = requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1', headers=headers)



