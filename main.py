import requests
city = "Moscow,RU"
appid = "7cc65a5b04e0860f6b847bfc1c941d2d"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': 'Moscow', 'units': 'metric', 'lang': 'ru', 'APPID': '7cc65a5b04e0860f6b847bfc1c941d2d'})
data = res.json()
print("Город:",'Moscow' )
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': 'Moscow', 'units': 'metric', 'lang': 'ru', 'APPID': '7cc65a5b04e0860f6b847bfc1c941d2d'})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("____________________________")