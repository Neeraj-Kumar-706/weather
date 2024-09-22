from envvar import key
import requests
api_key = key("ow_key")
#api_key = ''
print(api_key)
def weather_flag():
    print(200)
def weather(city):
    global api_key
    city = city
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response=requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        temp_min=data['main']['temp_min']
        temp_max=data['main']['temp_max']
        feel_like=data['main']['feels_like']
        print(f'Temperature: {temp} K')
        print(f'Description: {desc}')
        return temp,desc,feel_like
    else:
        print('Error fetching weather data')
#weather_flag()
weather('delhi,in')