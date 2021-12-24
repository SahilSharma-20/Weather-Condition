%reset -f

import requests, json

import gtts

import demoji

import os

from playsound import playsound

cities = input('Enter Number_of_cities:')

for i in range(int(cities)):    

    api_key = "db9f053143446cc58b988adc4959b3c2"

    # base_url variable to store url

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

 

    city_name = input("Enter city name : ")

 

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

 

    response = requests.get(complete_url)

 

    x = response.json()

    if  x["cod"] != "404":

        y = x["main"]

        current_temperature = y["temp"]-273.15

        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

 

        print(" Temperature (in celsius unit) =" +

                    str(round(current_temperature,2))

                        + " °C "

          "\n atmospheric pressure (in hPa unit) = " +

                    str(current_pressure) + " hPa "

          "\n humidity (in percentage) = " +

                    str(current_humidity) + " % "

          "\n description = " +

                    str(weather_description))

    else:

        print(" City Not Found ")

    Sunny = "😰"

    Cool = "🤧"

    language="en"

    if current_temperature >27 and current_temperature < 30:

        print("Sunny="+str(demoji.findall(Sunny)))

        txt = gtts.gTTS("Sunny",lang=language,slow=False)

        txt.save("media.mp3")    

        playsound("media.mp3")

    else:

        print("Cool="+str(demoji.findall(Cool)))

        txt = gtts.gTTS("Cool")

        txt.save("media.mp3")    

        playsound("media.mp3")

    os.remove('media.mp3')

   

    txt = gtts.gTTS('Display wheather report for:-'+ city_name)

    txt.save("media.mp3")    

    playsound("media.mp3")

    os.remove('media.mp3')

    url = 'https://wttr.in/{}'.format(city_name)

    res = requests.get(url)

    print(res.text)
