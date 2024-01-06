import requests
from machine import Pin
from time import sleep
import dht
import network

sensor = dht.DHT11(Pin(18))

 
wifi_name = "Ucebna13"
wifi_password = "jablko987"
 
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

if sta_if.isconnected() == False:
    print("Connecting...")
    
    sta_if.connect(wifi_name, wifi_password)
 


while True:
  gc.collect()
  try:
    sleep(2)
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    t_str = str(t)
    h_str = str(h)
    print('Temperature: %3.1f C' % t)
    print('Humidity: %3.1f %%' % h)
    print(t_str)
    print(h_str)


    try:
        requests.get(f"https://maker.ifttt.com/trigger/eventTrigger/with/key/b0NctliCtEbkGm1hgQy5dn?value1={t_str}C&value2={h_str}%")
    except Exception as e:
        print("Error making request:", str(e))

  except OSError as e:
    print('Sensor Reading Failed')