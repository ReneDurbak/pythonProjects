import requests
import matplotlib.pyplot as plt
from datetime import datetime,  timedelta
  
x = [] 
y = []



def pocasie(lat, lon):
    url = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid=c10d9a7ca0369f89897dd1265150a60a").json()
    min = 1000
    max = 0
    isRain = False
    isCold = False

    for day in url['list']:
        temp = day['main']['temp']
        date = datetime.fromtimestamp(day["dt"])
        x.append(date)
        y.append(temp)
        tempMin = day['main']['temp_min']
        tempMax = day['main']['temp_max']

        if(tempMin < min): min = tempMin
        if(tempMax > max): max= tempMax

        if(day['weather'][0]['main'] == 'Rain'): isRain = True
        if(temp < 10): isCold = True

        title = f"{'Vezmi si dazdnik' if isRain else ''}{' a vezmi si aj sveter' if isCold else ''}"
        if not isCold and not isRain:
            title = "Bude dobre neber nic."

        additionalText = ''

        if isRain:
            additionalText += 'Bude pršať, tak si prosím vezmi dáždnik!'
            if isCold:
                additionalText += ' A vezmi si aj sveter!'
        else:
            if isCold:
                additionalText = 'Prosím si vezmi sveter'

        dateISOformat = date.isoformat()
        requests.get(f"https://maker.ifttt.com/trigger/kalendarTrigger/with/key/b0NctliCtEbkGm1hgQy5dn?value1={dateISOformat}&value2={title}&value3={additionalText}")



def pocasieNaDalsiDen(lat, lon):
    url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=sk&units=metric&APPID=c10d9a7ca0369f89897dd1265150a60a").json()
    url2 = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&lang=sk&units=metric&appid=c10d9a7ca0369f89897dd1265150a60a").json()

    for day in url2['list']:
        if(day['weather'][0]['main'] == 'Rain'): isRain = True

    minTemp = url['main']['temp_min']
    maxTemp = url['main']['temp_max']
    description = url['weather'][0]['description']
    current_date = datetime.now()
    tomorrowDate = current_date + timedelta(1)
    
    title = "Celodenna predpoved"
    additionalText = f"Dnes bude {description} s teplotami {minTemp} az {maxTemp}. {'Budete potrebovat dazdnik' if isRain else 'Nebudete potrebovat dazdnik.'}"

    requests.get(f"https://maker.ifttt.com/trigger/kalendarTrigger/with/key/b0NctliCtEbkGm1hgQy5dn?value1={tomorrowDate.strftime('%Y-%m-%dT04:30:00Z')}&value2={title}&value3={additionalText}")


    



def weatherGraph():
    plt.plot(x, y, label = "line 1") 
    
    plt.ylabel('Teplota') 
    plt.xlabel('Datum') 

    plt.title('Predpoved pocasia') 
    plt.legend() 

    plt.show()




def main():
    lat = input("latitude: ")
    lon = input("longtitude: ")

    pocasie(lat,lon)
    weatherGraph()
    pocasieNaDalsiDen(lat, lon)
    

    
   



main()

 