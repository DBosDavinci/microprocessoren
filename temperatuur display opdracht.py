from machine import Pin
import dht
from utime import sleep
import _thread

segments = (0,1,2,3,4,5,6,7)

patterns = [
    (1, 1, 1, 1, 1, 1, 0, 0),
    (0, 1, 1, 0, 0, 0, 0, 0),
    (1, 1, 0, 1, 1, 0, 1, 0),
    (1, 1, 1, 1, 0, 0, 1, 0),
    (0, 1, 1, 0, 0, 1, 1, 0),
    (1, 0, 1, 1, 0, 1, 1, 0),
    (1, 0, 1, 1, 1, 1, 1, 0),
    (1, 1, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1, 0),
    (1, 1, 1, 0, 0, 1, 1, 0)
]

pins = [Pin(seg, Pin.OUT) for seg in segments]

d1 = Pin(15, Pin.OUT, value=1)
d2 = Pin(14, Pin.OUT, value=1)
d3 = Pin(13, Pin.OUT, value=1)
d4 = Pin(12, Pin.OUT, value=1)

sensor = dht.DHT11(Pin(27))

def display_digit(display, digit):    
    pattern = patterns[digit]
    
    for i in range(8):
        pins[i].value(pattern[i])
    
    display.value(0)
    
    display.value(1)
    
temperature = [2,5]

def updateDisplay():
    while True:
        display_digit(d1, int(temperature[0]))
        display_digit(d2, int(temperature[1]))
    
def readTemp():
    global temperature
    while True:
        sensor.measure() 
        temp = sensor.temperature()
        temperature = list(str(temp))
        
        hum = sensor.humidity()
        print(f'temp: {temp} C')
        print(f'hum: {hum} %')
        sleep(5)
        
second_thread = _thread.start_new_thread(readTemp, ())

updateDisplay()


