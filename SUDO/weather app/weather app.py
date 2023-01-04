import datetime as dt
import requests

city = input("Enter a City: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?q="
api_key = open('apiKey', 'r').read()
url = base_url + city + "&appid=" + api_key

response = requests.get(url).json()
def temperature_scale(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit

kelvin = response['main']['temp']
celsius, fahrenheit = temperature_scale(kelvin)
feels_like = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = temperature_scale(kelvin)
humidity = response['main']['humidity']
wind_speed = response['wind']['speed']
region = response['sys']['country']
pressure = response['main']['pressure']
weather_description = response['weather'][0]['description']
sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"City: {city}")
print(f"Country: {region}")
print(f"Temperature in {city}: {celsius:.2f}°C or {fahrenheit:.2f}F")
print(f"Temperature in {city} Feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}F")
print(f"Humidity in {city}: {humidity}%")
print(f"Sunrise Time in {city}: {sunrise}, Local Time")
print(f"Sunset Time in {city}: {sunset}, Local Time")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Pressure: {pressure}Kpa")
print(f"Description: {weather_description}")
