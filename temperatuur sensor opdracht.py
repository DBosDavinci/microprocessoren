from machine import Pin
import dht
from utime import sleep

sensor = dht.DHT11(Pin(27))
while True:
    sensor.measure() 
    temp = sensor.temperature()
    print(list(str(temp)))
    hum = sensor.humidity()
    print(f'temp: {temp} C')
    print(f'hum: {hum} %')
    sleep(5)