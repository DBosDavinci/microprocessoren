from machine import Pin
import time

light = Pin(2, Pin.OUT)
button1 = Pin(28, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(27, Pin.IN, Pin.PULL_DOWN)

on = False

while True:
    if button1.value():
        on = not on
        light.value(on)
        time.sleep(0.2)            
    if button2.value():
        light.value(True)
    else:
        if not button1.value():
            light.value(on) 