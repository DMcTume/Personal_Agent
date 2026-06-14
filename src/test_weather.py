import requests

api_key = "dd96c758f7dbcb4110d884d230ebc61f"
root_weather = "http://api.openweathermap.org/data/2.5/weather?"
root_geo = "http://api.openweathermap.org/geo/1.0/direct?"
city_name = "NYC"
limit = 5

# Get lat, lon of city_name:
url = f"{root_geo}q={city_name}&limit={limit}&appid={api_key}"

geo_info = requests.get(url).json()
lat = geo_info[0]["lat"]
lon = geo_info[0]["lon"]

# Get weather info
url = f"{root_weather}lat={lat}&lon={lon}&appid={api_key}"
print(lat, lon)
