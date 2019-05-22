import requests
import json
from datetime import datetime

class Owm(object):
    """
    class to handle open weather map api calls
    """
    def __init__(self):
        """ class constructor (set api key)"""
        self.api_key = "a993b0bfcf1516da9ce51bb60c2da2d6"
        self.server = "https://api.openweathermap.org/data/2.5/{0}?id={1}&appid={2}".format("{0}","{1}",self.api_key)

    def api_call(self,url):
        """ call open weather map api with request """
        response = requests.post(url)
        return response.json()

    def api_fake_weather(self,url):
        """ return fake call for dev purposes """
        dic = {'coord': {'lon': 1.44, 'lat': 43.6}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 291.77, 'pressure': 1019, 'humidity': 59, 'temp_min': 289.15, 'temp_max': 293.71}, 'visibility': 10000, 'wind': {'speed': 2.1, 'deg': 260}, 'clouds': {'all': 0}, 'dt': 1558517488, 'sys': {'type': 1, 'id': 6467, 'message': 0.0052, 'country': 'FR', 'sunrise': 1558498988, 'sunset': 1558552735}, 'id': 6453974, 'name': 'Toulouse', 'cod': 200}
        return dic

    def api_fake_forecast(self,url):
        """ return fake call for dev purposes """
        with open('fake_forecast.json') as json_file:
            data = json.load(json_file)
        return data

    def get_city_id(self,city):
        """ Look for the city data base and returns the city id """
        with open('city.list.json') as json_file:
            data = json.load(json_file)
        for dico in data:
            if dico['name'].upper() == city.upper() : return dico['id']
        return None

    def parse_response(self,raw):
        """ Parse raw api response and return formated one """
        dic = {}
        dic['description'] = raw['weather'][0]['description']
        dic['humidity']    = raw['main']['humidity']
        dic['pressure']    = raw['main']['pressure']
        dic['temp']        = int(raw['main']['temp']-273.15)
        dic['temp_min']    = int(raw['main']['temp_min']-273.15)
        dic['temp_max']    = int(raw['main']['temp_max']-273.15)
        dic['wind_speed']  = raw['wind']['speed']
        dic['wind_dir']    = int(raw['wind']['deg'])
        dic['clouds']      = raw['clouds']['all']
        if 'visibility' in raw.keys(): dic['visibility']  = raw['visibility']
        if 'sunrise' in raw['sys'].keys(): dic['sunrise'] = datetime.fromtimestamp(raw['sys']['sunrise'])
        if 'sunrset' in raw['sys'].keys(): dic['sunset'] = datetime.fromtimestamp(raw['sys']['sunset'])
        return dic

    def get_weather(self,city):
        """ Get current weather for a city """
        city_id = self.get_city_id(city)
        url = self.server.format('weather',city_id)
        rep = self.api_call(url.format(city_id,self.api_key))
        rep = self.api_fake_weather(url.format(city_id,self.api_key))
        dic = self.parse_response(rep)
        return dic

    def get_forecast(self,city):
        """ Get current weather for a city """
        city_id = self.get_city_id(city)
        url = self.server.format('forecast',city_id)
        rep = self.api_call(url.format(city_id,self.api_key))
        #rep = self.api_fake_forecast(url.format(city_id,self.api_key))
        forecast = {}
        for element in rep['list']:
            day = datetime.fromtimestamp(element['dt']).strftime('%A')
            forecast[day] = self.parse_response(element)

        return forecast


if __name__ == "__main__":
    owm = Owm()
    weather = owm.get_weather('Toulouse')

    for key in weather:
        print(key,weather[key])

    forecast = owm.get_forecast('Toulouse')
    print(forecast)
