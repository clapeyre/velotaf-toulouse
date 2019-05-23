from Owm import Owm
import roulibre as rou

def update_today(weather):
    """ Update today page with weather conditions """
    logo = rou.weather_img[weather['description']]
    lines = [rou.today_header.format(logo)]

    # Add temperature item : 5   -> progress bar = 0%
    #                        40  -> progress bar = 100%
    progress_bar = max(0,min(((weather['temp_min']+weather['temp_max']/2)-5)/35,1),0)*100
    lines.append(rou.today_item.format("Temperatures",
                                       "mini {0}, maxi= {1}°C".format(weather['temp_min'],weather['temp_max']),
                                       progress_bar))

    # Add rain item
    rain_description = rou.rain_description.get(weather['description'],'Pas de pluie')
    rain_intensity   = rou.rain_progress_bar.get(weather['description'], 0)
    lines.append(rou.today_item.format(rain_description," ",rain_intensity))

    # Add wind item: 0 km/h -> progress bar = 0%
    #               40 km/h -> progress bar = 100%
    wind_dir = rou.wind_dir[weather['wind_dir']]
    progress_bar = min((weather['wind_speed'])/40,1)*100
    lines.append(rou.today_item.format("Vent",wind_dir,progress_bar))

    # Add humidity item
    lines.append(rou.today_item.format("Humiditée"," ",weather['humidity']))

    # Add visibility item :
    visibility = rou.visibility[weather['visibility']]
    progress_bar = weather['visibility']/100
    lines.append(rou.today_item.format("Visibilitée"," ",weather['visibility']))

    with open("../data/today.yml","w") as fid:
        fid.writelines(lines)

def update_forecast(forecast):
    """ Update forecast page with weather forecast """
    import time
    today = time.strftime('%A')
    print(today)

    week_summary = "Bonne semaine pour le vélo"
    lines = [ rou.forecast_header.format(week_summary)]

    for day in forecast:
        text = []
        if not day == today:
            jour = rou.jour[day]
            index = 0
            if forecast[day]['temp'] < 10 :
                text.append('Temperature faible, couvrez vous.')
                index += 1
            if 'rain' in forecast[day]['description']:
                text = ['Pluie prévue']
                index += 3
            if len(text) == 0:
                text = ['Belle journée, prend ton vélo']
            lines.append(rou.forecast_item.format(rou.forecast_img[index],jour,'. '.join(text)))

    with open("../data/forecast.yml","w") as fid:
        fid.writelines(lines)

if __name__ == "__main__":
    owm = Owm()

    # Today page
    print("Updating today weather")
    weather = owm.get_weather('Toulouse')
    update_today(weather)

    # Forecaste page
    print("Updating weather forecast")
    forecast = owm.get_forecast('Toulouse')
    update_forecast(forecast)
