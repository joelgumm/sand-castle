# Import necessary modules
import machine
import time

led = machine.Pin(25, machine.Pin.OUT)


def run():
    # Configure the onboard LED (GP25) as an output

    led.on()
    time.sleep(5)
    led.off()
    time.sleep(.2)
    led.on()
    time.sleep(1)
    led.off()
