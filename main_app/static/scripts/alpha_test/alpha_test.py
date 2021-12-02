import requests
import os
from datetime import datetime
from dateutil import parser
from dotenv import load_dotenv

load_dotenv()

# KEY INPUTS
ticker = 'IBM'
apikey = os.getenv("API_KEY_ALPHA")
data_type = 'GLOBAL_QUOTE'

# Build URL
base_url = 'https://www.alphavantage.co/query?'
query_function = f'function={data_type}'
query_symbol = f'symbol={ticker}'
query_key = f'apikey={apikey}'

url = f'{base_url}&{query_function}&{query_symbol}&{query_key}'

# Get JSON data: 
r = requests.get(url)
data = r.json()
# print(data)

# Get price and date
field_type = 'Global Quote'
field_name_1 = '07. latest trading day'
field_name_2 = '05. price'

# String output
price_str = data[field_type][field_name_2]
date_str = data[field_type][field_name_1]

# Price: Format
price_float = float(price_str)
price_decimal = round(price_float,2)

# Date: Format
# date = parser.parse(date_str)
date = datetime.strptime(date_str, "%Y-%m-%d")


print(price_decimal)
print(date)

# Scalable Query

# # Build Query by destructuring the dictionary
# query = ''
# for key, value in query_dict.items():
#     query += key + '=' + value + '&'

# # Post-process Query: Remove last '&'
# query = query[:-1]

# # Build URL: base + query

# url = base_url + query



## NOTE: Obsolete stuff
