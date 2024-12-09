from machine import Pin
import utime

print("running")

green = Pin(17, Pin.OUT)
yellow = Pin(21, Pin.OUT)
red = Pin(27, Pin.OUT)

trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)
   
while True:
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
       signaloff = utime.ticks_us()
    while echo.value() == 1:
       signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    if distance <= 10:
        break

redTime = utime.ticks_ms()

while utime.ticks_diff(utime.ticks_ms(), redTime) <= 5000:
    red.on()

red.off()

yellowTime = utime.ticks_ms()

while utime.ticks_diff(utime.ticks_ms(), yellowTime) <= 2000:
    yellow.on()
    
yellow.off()

greenTime = utime.ticks_ms()

while utime.ticks_diff(utime.ticks_ms(), greenTime) <= 5000:
    green.on()

green.off()