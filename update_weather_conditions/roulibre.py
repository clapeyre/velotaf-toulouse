global_description = { 'clear sky'              : 'Temps clair',
                       'scattered clouds'       : 'Nuages épars',
                       'broken clouds'          : 'Quelques nuages',
                       'overcast clouds'        : 'Nombreux nuages',
                       'light rain'             : 'Pluie légère',
                       'moderate rain'          : 'Pluie modérée',
                       'heavy intensity rain'   : 'Pluie forte',
                       'very heavy rain'        : 'Pluie très forte'}

weather_img = {}
weather_img['clear sky']            = 'images/weather/Sunny.png'
weather_img['broken clouds']        = 'images/weather/Overcast.png'
weather_img['scattered clouds']     = 'images/weather/Overcast.png'
weather_img['overcast clouds']      = 'images/weather/Overcast.png'
weather_img['light rain']           = 'images/weather/Rainy.png'
weather_img['moderate rain']        = 'images/weather/Rainy.png'
weather_img['heavy intensity rain'] = 'images/weather/Rainy.png'
weather_img['very heavy rain']      = 'images/weather/Rainy.png'

forecast_img = dict([(n,'images/green_bike.png') for n in range(0,1)] +
                    [(n,'images/orange_bike.png') for n in range(1,3)] +
                    [(n,'images/red_bike.png') for n in range(3,10)])

rain_description = {'no rain'                : 'Pas de pluie',
                    'light rain'             : 'Pluie légère',
                    'moderate rain'          : 'Pluie modérée',
                    'heavy intensity rain'   : 'Pluie forte',
                    'very heavy rain'        : 'Pluie très forte'}

temp_description = dict([(n,'temperatures froides')  for n in range(-10,5)] +
                        [(n,'temperatures fraiches') for n in range(5,15)] +
                        [(n,'temperatures douces')   for n in range(15,25)] +
                        [(n,'temperatures chaudes')   for n in range(25,50)])

rain_progress_bar = {'no rain':0,'light rain': 20,'moderate rain': 50,'heavy intensity rain':90,'very heavy rain':100}

wind_dir = dict([(n,'Nord')       for n in range(0,23)] +
                [(n,'Nord-Est')   for n in range(23,68)] +
                [(n,'Est')        for n in range(68,113)] +
                [(n,'Sud-Est')    for n in range(113,158)] +
                [(n,'Sud')        for n in range(158,203)] +
                [(n,'Sud-Ouest')  for n in range(203,248)] +
                [(n,'Ouest'    )  for n in range(248,293)] +
                [(n,'Nord-Ouest') for n in range(293,338)] +
                [(n,'Nord')       for n in range(338,360)])

visibility = dict([(n,'Nulle') for n in range(0,1000)] +
                  [(n,'Faible') for n in range(1000,2000)] +
                  [(n,'Bonne') for n in range(5000,10001)])

jour = {'Monday':'Lundi','Tuesday':'Mardi','Wednesday':'Mercredi','Thursday':'Jeudi',
        'Friday':'Vendredi','Saturday':'Samedi','Sunday':'Dimanche'}

next_day = {'Monday':'Tuesday','Tuesday':'Wednesday','Wednesday':'Thursday','Thursday':'Friday',
            'Friday':'Saturday','Saturday':'Sunday','Sunday':'Monday'}

morning        = 'Matinée '
day            = 'Journée '
cold           = 'fraiche, couvrez vous.'
slight_wet     = 'Quelques gouttes de prévues.'
wet            = 'Pluie préuve ... sortez le ciret.'
sunny          = 'ensoleillée'
hot            = 'chaude'

today_header ="""enable : true
heading : Aujourd’
headingSpan : hui
title : {0}
content : {1}
image : {2}
weatherItem : """

today_item = """
  - itemNumber : {0}
    itemName : {1}
    itemPercent : {2}%
"""

forecast_header = """enable : true
heading : Les prochains
headingSpan : jours
resume : {0}
forecastItem :
"""

forecast_item = """
  - icon : {0}
    title : {1}
    content : {2}
"""
