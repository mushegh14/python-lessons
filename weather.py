import argparse
import requests

parser = argparse.ArgumentParser(description="exnaki tesutyun")

parser.add_argument("-c","--city",required=True,help="mutqarir qaxaqi anunn")

parser.add_argument("-x", "--parameter",choices=["temperature", "humidity", "wind"],help="cucadrel konkret exanakayin paymanern")


data = parser.parse_args()

print("City:", data.city)

url = "https://geocoding-api.open-meteo.com/v1/search"

my_params = {"name": data.city}

response = requests.get(url, params=my_params)

geo_data = response.json()


laynutyun = geo_data['results'][0]['latitude']

erkarutyun = geo_data['results'][0]['longitude']


weather_url = "https://api.open-meteo.com/v1/forecast"

weather_params = {
    "latitude": laynutyun,
    "longitude": erkarutyun,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

weather_response = requests.get(weather_url, params=weather_params)

weather_data = weather_response.json()

temperature = weather_data["current"]["temperature_2m"]
humidity = weather_data["current"]["relative_humidity_2m"]
wind_speed = weather_data["current"]["wind_speed_10m"]

weather_info = {
    "temperature": {
        "label": "Temperature",
        "value": temperature
    },
    "humidity": {
        "label": "Humidity",
        "value": humidity
    },
    "wind": {
        "label": "Wind speed",
        "value": wind_speed
    }
}

if data.parameter:
    selected = weather_info[data.parameter]
    print(selected["label"] + ":", selected["value"])
else:
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Wind speed:", wind_speed)