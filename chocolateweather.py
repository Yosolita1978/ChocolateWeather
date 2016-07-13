import pyowm
from security_info import *

owm = pyowm.OWM(API_KEY)

def get_weather(place):
    obs = owm.weather_at_place(place)
    weather = obs.get_weather()
    return weather


def if_clouds(place):
    weather = get_weather(place) 
    clouds = weather.get_clouds()
    if clouds >=5:
        karl = weather.get_detailed_status()
        return karl

def forecast_sun(place):
    forecast = owm.daily_forecast(place)
    sun = forecast.will_have_sun()
    if sun == False:
        return "What do you expect from San Francisco?. Let's go for some chocolate"
    else:
        return "This is a miracle. You will see the sun! Let's Eat chocolate to celebrate" 

def main():

    print "Hello, there. Let's check if the weather is nice."
    city = ("""Let's check the weather in San Francisco, CA. Type Y or N """)
    weather_city = raw_input(city)
    place = "San Francisco, CA"
    if weather_city == "Y":
        w = get_weather(place)
        celsius = w.get_temperature("celsius")
        print celsius
        print ("Wow! Apparently the odds are greater that you would have %s for today" %(celsius["temp"]))
        print forecast_sun(place)
        prompt1 = ("Neverless, let's check one more time if you need that chocolate. Press Enter when you're ready """)
        user_choice1 = raw_input(prompt1)
        if user_choice1 == "":
            lucky = if_clouds(place)
            print ("Lucky you, you will have %s, so you really need that chocolate" %(lucky))

    else:
        print ("If you don't live in %s, eat that chocolate, it's cheaper" %(place))

        



if __name__ == '__main__':
  main()
