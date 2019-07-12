from gpiozero import LED
from time import sleep

import pyowm

def Weather_Forecast():
    city = input("Enter Name of City with space :- ")
    country = input("Enter Name of Country :- ")

    apikey = '51c6723dd2f51626dd33896729e79676'
    owm = pyowm.OWM(apikey)
    combine = city + country
    observation = owm.weather_at_place(combine)
    w = observation.get_weather()



    winds = w.get_wind()
    humidities = w.get_humidity()
    tempreture = w.get_temperature()
    presh = w.get_pressure()
    clud = w.get_clouds()
    ran = w.get_rain()
    snoww = w.get_snow()

    print(" The weather information for " + city + ", " + country)
    
    print("The wind result is :- ", winds )
    print("The humidity result is :- ", humidities)
    print("The tempreture is :- ", tempreture )
    print("The pressure is :- ", presh)
    print("The cloud coverage is :- ", clud)
    print("The cloud rain volume is :- ", ran)
    print("The cloud snow volume is :- ", snoww)



led = LED(17)#yellow
led1 = LED(18)#red
led2 = LED(27)#green

while True:
    led1.on()
    sleep(5)
    led1.off()
    sleep(1)
    
    led.on()
    sleep(2)
    led.off()
    sleep(1)
    
    
    led2.on()
    sleep(5)
    led2.off()
    sleep(1)
