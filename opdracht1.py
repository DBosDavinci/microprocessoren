from machine import Pin
from utime import sleep

print("Hello, Pi Pico!")

led = Pin(2, Pin.OUT)
while True:
  led.on()