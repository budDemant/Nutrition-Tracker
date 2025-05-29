import os
import requests
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DBNAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST")
    )
    

def search_food(query):
    API_KEY = os.environ.get("USDA_API_KEY")
    if not API_KEY:
        print("USDA_API_KEY not set in environment.")
        return
    
    url_search = "https://api.nal.usda.gov/fdc/v1/foods/search"
    params = {"query": query, "pageSize": 1}
    headers = {'X-Api-Key': API_KEY}
    
    try:
        response_search = requests.get(url_search, params=params, headers=headers)
        response_search.raise_for_status() # check for 200 (OK)
        
        foods = response_search.json().get("foods", [])
        if not foods:
            print(f"No results found for '{query}'.")
            return
        
        food = foods[0]
        fdc_id = food.get('fdcId')
        description = food.get('description')
        
        url_id = f"https://api.nal.usda.gov/fdc/v1/food/{fdc_id}"
        response_id = requests.get(url_id, headers=headers)
        response_id.raise_for_status()
        data_id = response_id.json()
        serving_size = data_id.get('servingSize')
        unit = data_id.get('servingSizeUnit')
        
        print(f"Name: {description} | FDC ID: {fdc_id} | Serving Size: {serving_size} {unit} ")
    except requests.RequestException as e:
        print("API request failed:", e)
        
if __name__ == "__main__":
    # Test DB connection
    try:
        conn = get_connection()
        print("Database connection successful!")
        conn.close()
    except Exception as e:
        print("Database connection failed:", e)

    search_term = input("Search for a food: ")
    search_food(search_term)
    
    


