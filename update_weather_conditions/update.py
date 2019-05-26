from Owm import Owm
import roulibre as rou

def update_today(weather):
    """ Update today page with weather conditions """
    lines = []

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

    # add header
    logo     = rou.weather_img[weather['description']]
    title    = '{0}, {1}'.format(rou.global_description[weather['description']],
                                 rou.temp_description[weather['temp']])
    subtitle = ' '
    head_lines = [rou.today_header.format(title,subtitle,logo)]

    with open("../data/today.yml","w") as fid:
        fid.writelines(head_lines)
        fid.writelines(lines)

def update_forecast(forecast):
    """ Update forecast page with weather forecast, A REVOIR !!  """
    import time
    day = time.strftime('%A')
    day_index = []
    lines = []
    for day_idx in range(len(forecast)):
        day = rou.next_day[day]
        text = []
        index = 0

        jour = rou.jour[day]
        hours = [hour for hour in forecast[day]]
        hours.sort(reverse=True)
        for hour in hours:
            if hour < 12: rain_daytime = rou.morning
            else : rain_daytime = rou.day
            if forecast[day][hour]['temp'] < 10 :
                if not rou.cold in text:
                    text.append(rain_daytime)
                    text.append(rou.cold)
                    index += 1
        if index == 0: rain_daytime = rou.day

        for hour in hours:
            desc = forecast[day][hour]['description']
            if hour < 12: daytime = rou.morning
            else : daytime = rou.day

            if 'rain ' in desc and not desc in ['light rain','moderate rain']:
                if not rou.wet in text:
                    #if not daytime == rain_daytime: text.append(daytime)
                    text.append(rou.wet)
                    index += 3

        for hour in hours:
            desc = forecast[day][hour]['description']
            if hour < 12: daytime = rou.morning
            else : daytime = rou.day
            if not rou.wet in text:
                if  desc in ['light rain','moderate rain']:
                    if not rou.slight_wet in text:
                        #if not daytime == rain_daytime: text.append(daytime)
                        text.append(rou.slight_wet)
                        index += 1
        if index == 0:
            text = ['Belle journée, sort le vélo.']
        lines.append(rou.forecast_item.format(rou.forecast_img[index],jour,'. '.join(text)))
        day_index.append(index)

    if sum(day_index) <3:
        week_summary = "Bonne semaine pour le vélo"
    elif sum(day_index) <10:
        week_summary = "Semaine mitigée mais gardez la motivation"
    else:
        week_summary = "Pas une super semaine pour le vélo mais restze motivés"

    header = [ rou.forecast_header.format(week_summary)]

    with open("../data/forecast.yml","w") as fid:
        fid.writelines(header)
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
