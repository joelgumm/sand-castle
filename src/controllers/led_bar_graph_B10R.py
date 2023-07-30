import machine
import utime

pin = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
led = []
for i in range(10):
    led.append(None)
    led[i] = machine.Pin(pin[i], machine.Pin.OUT)


# def getLeds():
#     return led
# while True:
#     for i in range(10):
#         led[i].toggle()
#         utime.sleep(0.2)

# # Define the LED pins
# led_pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# # Define the temperature range and the temperature increment
# temp_range = range(5, 55, 5)
# temp_increment = 5
#
# # Initialize the LED pins as outputs
# leds = [Pin(pin, Pin.OUT) for pin in led_pins]
#
# # Initialize the temperature sensor
# sensor_temp = ADC(4)
# conversion_factor = 3.3 / (65535)
#
# # Function to read the temperature from the onboard sensor
# def get_temperature():
#     reading = sensor_temp.read_u16() * conversion_factor
#     temperature = 27 - (reading - 0.706) / 0.001721
#     return temperature
#
# while True:
#     # Read the temperature from the sensor
#     temp = get_temperature()
#
#     # Determine the index of the temperature range that the current temperature falls within
#     index = int((temp - temp_range[0]) / temp_increment)
#
#     # Turn on the appropriate LEDs based on the index
#     for i in range(len(leds)):
#         if i <= index:
#             leds[i].value(1)
#         else:
#             leds[i].value(0)
#
#     # Wait for a short period before updating the LED display again
#     utime.sleep(0.5)
