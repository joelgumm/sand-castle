from machine import Pin, SPI
from lib import max7219
from time import sleep

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)

display = max7219.Matrix8x8(spi,cs,1)

display.brightness(1)

scrolling_message = "SHELDON"
length = len(scrolling_message)
column = (length * 8)

display.fill(0)
display.show()
sleep(1)

while True:
    for x in range(32, -column, -1):
        display.fill(0)
        display.text(scrolling_message ,x,0,1)
        display.show()
        sleep(0.1)