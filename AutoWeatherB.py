import requests
import json

api_key = "b39dbc2c95d91b47ac546f193b3102be"
city = "Lagos"
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=b39dbc2c95d91b47ac546f193b3102be&appid=%s&units=metric" .format(city)

response = requests.get(url)
data = json.loads(response.text)
print(data)
