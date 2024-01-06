import machine
import time

zlta = machine.Pin(26, machine.Pin.OUT)
cervena = machine.Pin(25, machine.Pin.OUT)
zelena = machine.Pin(14, machine.Pin.OUT)

led = [cervena, zlta, zelena]



def blikanie():
    
    for i in range(0, 3):
        zelena.value(0)
        time.sleep(1)
        zelena.value(1)
        time.sleep(1)
    
    
#     zelena.value(0)
#     time.sleep(1)
#     
#     zelena.value(1)
#     time.sleep(1)
#     
#     zelena.value(0)
#     time.sleep(1)
#     
#     zelena.value(1)
#     time.sleep(1)
#     
#     zelena.value(0)
#     time.sleep(1)
#     
#     zelena.value(1)
#     time.sleep(1)
#     
#     zelena.value(0)
    
    
def cervena_zlta_zelena():
    cervena.value(0)    
    zelena.value(0)
    
    cervena.value(1)
    time.sleep(5)
    
    zlta.value(1)
    time.sleep(2)
    
    cervena.value(0)
    zlta.value(0)
    
    zelena.value(1)
    time.sleep(10)
    
    
def zelena_zlta_cervena():
    zlta.value(1)
    time.sleep(3)
    zlta.value(0)
    

while True:
    
    cervena_zlta_zelena()
    
    blikanie()
    zelena.value(0)
    
    zelena_zlta_cervena()
    
    
    
    
    
    
    
    
    
    
    
