import requests
import json

api_key = "73c857148b6be9a432143dface4a3a59"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
cityName = input("Enter your city name :-  ")

url = base_url + " Api key" + api_key + "City Name :- " + cityName

response = requests.get(url)
x = response.json()
if x["cod"] != "404":

  y = x["main"]

  current_temperature = y["temp"]

  current_pressure = y["pressure"]

  current_humidity = y["humidity"]

  z = x["weather"]
  weather_description = z[0]["description"]

  print(" Temperature (in kelvin unit) = " + str(current_temperature) +
        "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) +
        "\n humidity (in percentage) = " + str(current_humidity) +
        "\n description = " + str(weather_description))

else:
  print(" City Not Found ")
