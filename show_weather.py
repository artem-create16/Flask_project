import requests


def get_weather_forecast(city):
    result_forecast_weather = []
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                            params={'q': city, 'units': 'metric', 'lang': 'ru',
                            'APPID': '271b7de2d6a5fced172919a774f90d00'})
        data = res.json()
        for i in data['list']:
            step = (i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
            result_forecast_weather.append(step)
    except Exception as e:
        print("Exception (forecast):", e)
    return result_forecast_weather


def get_currently_weather(city):
    try:
        result = requests.get("http://api.openweathermap.org/data/2.5/weather",
                              params={'q': city, 'units': 'metric', 'lang': 'ru',
                                      'APPID': '271b7de2d6a5fced172919a774f90d00'})
        data = result.json()
        return '{0:+3.0f}'.format(data['main']['temp']), data['weather'][0]['description']

    except Exception as e:
        print("Exception (forecast):", e)