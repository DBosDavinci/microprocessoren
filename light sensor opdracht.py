from machine import Pin
from machine import ADC
from utime import sleep

adc = ADC(27)
led = Pin(2, Pin.OUT)
while True:
    digital_value = adc.read_u16()     
    if digital_value >= 60000:
        led.off()        
    else:
        led.on()