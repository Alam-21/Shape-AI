'''Program to recieve daily weather report for third party api and store it in a text file'''

import requests
from datetime import datetime

api_key = '2fb271a4ff593749f9bd28448a203bb2'
city = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = str(api_data['main']['humidity'])
wind_spd = str(api_data['wind']['speed'])
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#writing the weather reports into text file 
with open("weather_report.txt","w") as f:
    f.write("="*60)
    f.write("\nWeather Reports for - {}  || {}".format(city.upper(), date_time)+ '\n')
    f.write("="*60)
    f.write ("\nCurrent temperature is: {:.2f} deg C".format(temp_city)+'\n')
    f.write ("Current weather desc  :"+ weather_desc +'\n')
    f.write ("Current Humidity      :"+ hmdt + '%'+'\n')
    f.write ("Current wind speed    :"+ wind_spd + 'kmph')

