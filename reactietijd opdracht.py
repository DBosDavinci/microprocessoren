from machine import Pin
import utime
import random
import sys

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)
button1 = Pin(18, Pin.IN, Pin.PULL_UP)
button2 = Pin(19, Pin.IN, Pin.PULL_UP)
button3 = Pin(20, Pin.IN, Pin.PULL_UP)

setup = [[led1, button1], [led2, button2], [led3, button3]]
    
def startTimer(setup):
    led = setup[0]
    button = setup[1]
    time = utime.ticks_ms()
    while True:
        if utime.ticks_diff(utime.ticks_ms(), time) == random.randint(3000,10000):
            led.on()
            start = utime.ticks_ms()
            print("light on")

            while True:
                if button.value() == 1:
                    if utime.ticks_diff(utime.ticks_ms(), start) <= 1000:
                        continue
                    else:
                        print("too late")
                        led.off()
                        time = utime.ticks_ms()
                        break
                else:
                    print("reaction time:", utime.ticks_diff(utime.ticks_ms(), start))
                    led.off()
                    sys.exit()
while True:
    startTimer(setup[random.randint(0,2)])