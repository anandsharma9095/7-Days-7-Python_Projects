import requests
import os
from dotenv import load_dotenv

load_dotenv()

# getiing api from .env file 

API_KEY = os.getenv("WEATHER_KEY")
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"

print()
print('---------------------Weather App----------------------')
print()

city = input('Enter the name of the city : ')

params = {
    "q": city,
    "appid": API_KEY
}
response = requests.get(BASE_URL , params=params , timeout=5)

# also could have done this 
# request_url = f'{BASE_URL}?q={city}&appid={API_KEY}'
# but using the params kinda feels cool

# could have used try and except block but if else works fine for this small project

if response.status_code == 200:
    data = response.json()
    
    weather = data['weather'][0]['description']
    temp = round(data['main']['temp']-273.17 , 2)#*C
    feels_like = round(data['main']['feels_like'] -273.15 , 2)#*C
    pressure = data['main']['pressure'] #hPa
    wind_speed = data['wind']['speed'] #m/s
    humidity = data['main']['humidity'] #%
    
    
    print()
    print('Weather Condition : ',weather)
    print('Temperature       : ',temp , '*C')
    print('Feels Like        : ',feels_like , '*C')
    print('Pressure          : ',pressure , 'hPa')
    print('Wind Speed        : ',wind_speed , 'm/s')
    print('Humidity          : ',humidity , '%')
    
else:
    print("An Error Occured ............")


