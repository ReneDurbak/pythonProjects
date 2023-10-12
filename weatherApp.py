import requests
import time
from datetime import date, datetime

    

def getCurrentDateTime():
    return datetime.now().strftime('%d.%m.%Y, %H:%M')

def degrees(degree):
    directions = ['North', 'North-Northeast', 'Northeast', 'East-Northeast', 'East', 'East-Southeast', 'Southeast', 'South-Southeast', 'South', 'South-Southwest', 'Southwest', 'West-Southwest', 'West', 'West-Northwest', 'Northwest', 'North-Northwest']
    ix = round(degree / (360. / len(directions)))

    return directions[ix % len(directions)]

def weatherImage(weatherId):
    if(weatherId >= 200 and weatherId <= 232):
        return "https://openweathermap.org/img/wn/11d@2x.png"
    elif(weatherId >= 300 and weatherId <= 331):
        return "https://openweathermap.org/img/wn/09d@2x.png"
    elif(weatherId >= 500 and weatherId <= 504):
        return "https://openweathermap.org/img/wn/10d@2x.png"
    elif(weatherId >= 520 and weatherId <= 531):
        return "https://openweathermap.org/img/wn/09d@2x.png"
    elif(weatherId == 511 or (weatherId >= 600 and weatherId <= 622)):
        return "https://openweathermap.org/img/wn/13d@2x.png"
    elif(weatherId >= 701 and weatherId <= 781):
        return "https://openweathermap.org/img/wn/50d@2x.png"
    elif(weatherId == 800):
        return "https://openweathermap.org/img/wn/01d@2x.png"
    elif(weatherId == 801):
        return "https://openweathermap.org/img/wn/02d@2x.png"
    elif(weatherId == 802):
        return "https://openweathermap.org/img/wn/03d@2x.png"
    elif(weatherId == 803 or weatherId == 804):
        return "https://openweathermap.org/img/wn/04d@2x.png"


def sendToIFTTT(value1, value2):
    IFTTTKey = "b0NctliCtEbkGm1hgQy5dn"
    eventName = "weatherEvent"
    requestUrl = f"https://maker.ifttt.com/trigger/{eventName}/with/key/{IFTTTKey}?value1={value1}&value2={value2}"
    requests.get(requestUrl)
    time.sleep(0.5)

def updateWeatherData(cityName):
    weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&units=metric&APPID=c10d9a7ca0369f89897dd1265150a60a").json()
    
    if weatherData.get('cod') == 404:
        print("City not found")
        return
        
    city = weatherData['name']
    temperature = weatherData['main']['temp']
    feelsLike = weatherData['main']['feels_like']
    humidity = weatherData['main']['humidity']
    pressure = weatherData['main']['pressure']
    windSpeed = weatherData['wind']['speed']
    windDirection = degrees(weatherData['wind']['deg'])
    weatherDescription = weatherData['weather'][0]['description']
    weatherImageLink = weatherImage(weatherData['weather'][0]['id'])
    
    
    print("Updating data...")

        
    sendToIFTTT("B1", city)
    sendToIFTTT("D1", getCurrentDateTime())
    sendToIFTTT("C2", f"{temperature} °C")
    sendToIFTTT("A5", f"Feels like: {feelsLike} °C")
    sendToIFTTT("B4", f"{humidity} %")
    sendToIFTTT("C4", f"{pressure} hPa")
    sendToIFTTT("D4", f"{windSpeed} m/s")
    sendToIFTTT("D4", f"Direction: {windDirection}")
    sendToIFTTT("E4", f'%3DIMAGE("{weatherImageLink}")')
    sendToIFTTT("E5", weatherDescription)

    print("request to google sheets was successful")    
        

def main():
    city = input("Enter city name [without diacritics]: ")
    updateWeatherData(city)

main()