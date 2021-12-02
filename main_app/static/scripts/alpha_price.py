import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# KEY INPUTS
# ticker = 'IBM'
apikey = os.getenv("API_KEY_ALPHA")
data_type = 'GLOBAL_QUOTE'

# Get JSON data: 

def getStockPrice(ticker):
    # Build URL
    base_url = 'https://www.alphavantage.co/query?'
    query_function = f'function={data_type}'
    query_symbol = f'symbol={ticker}'
    query_key = f'apikey={apikey}'

    url = f'{base_url}&{query_function}&{query_symbol}&{query_key}'

    r = requests.get(url)
    data = r.json()

    # JSON Fields
    field_type = 'Global Quote'
    field_name_1 = '07. latest trading day'
    field_name_2 = '05. price'

    price = data[field_type][field_name_2]
    price_float = float(price)
    price_decimal = round(price_float,2)

    return price_decimal

def getStockDate(ticker):
    # Build URL
    base_url = 'https://www.alphavantage.co/query?'
    query_function = f'function={data_type}'
    query_symbol = f'symbol={ticker}'
    query_key = f'apikey={apikey}'

    url = f'{base_url}&{query_function}&{query_symbol}&{query_key}'

    r = requests.get(url)
    data = r.json()

    # JSON Fields
    field_type = 'Global Quote'
    field_name_1 = '07. latest trading day'
    field_name_2 = '05. price'

    date_str = data['Global Quote'][field_name_1]
    date = datetime.strptime(date_str, "%Y-%m-%d")

    return date