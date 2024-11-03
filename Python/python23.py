import urllib.request
import json

# Replace with your actual API key
api_key = '6d4e6a61ab501eecc6841e11b50856d8'
location = 'Bikaner,IN'
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

# Fetch data
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())
    temperature = data['main']['temp']
    print(f"Current temperature in {location}: {temperature}°C")


if temperature > 30:
    print("It's too hot outside.")
elif temperature < 15:
    print("It's too cold outside.")
else:
    print("It's perfect outside.")