# weather news

import pyttsx3
import datetime
import time 
import requests
import json

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(voice,n):
    engine.say(voice)
    engine.say(n)
    engine.runAndWait()

def greeting():
    hour=datetime.datetime.now().hour 
    if hour >=0 and hour<12:
        speak('Good Morning sir..',"")
    elif hour>=12 and hour <=18:
        speak('Good Afternoon sir..',"")
    else:
        speak("Good eveninng sir..","")
    time.sleep(0.4)
    speak("I'am jarvis","")

greeting()
try :
    user_input=input("Enter your city name ...\n")
except Exception as a:
    print(" Opps!! someting went wrong ..")
    print('Please try ....')

if __name__=='__main__':
    base_url=('https://api.openweathermap.org/data/2.5/weather?q=')   
    key="enter your api key"
    url=base_url+user_input+'&appid='+key
    weather_report=requests.get(url).text
    weather_report=json.loads(weather_report)
    print(weather_report)
    print("current Temperature is : ",weather_report['main']['temp'])
    speak("The current temperature is :",weather_report['main']['temp'])
    time.sleep(1)
    print("Current Humidity is :",weather_report['main']['humidity'])
    speak("Current Humidity is :",weather_report['main']['humidity'])
    time.sleep(1)
    print("current windspeed is :",weather_report['wind']['speed'])
    speak("current windspeed is :",weather_report['wind']['speed'])
    time.sleep(1)
print("Thanks for visiting us ","\n Have a good day")
speak("Thanks for visiting us ","\n Have a good day")


  