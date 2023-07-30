
from controllers import water_sensor_HW038 as water, led_bar_graph_B10R as bargraph
import utime

def map_moisture_range_to_led(number):
    # intervals of 100 represent sequential leds on bargraph
    threshold = 10  # Adjust this threshold value as needed
    index = max((number - threshold) // 75, 0)  # Ensure index is not less than zero
    print(index)
    return index


def display_bar_graph(sensor_value):
    led_array = bargraph.led
    # Map the sensor value to the array index
    index = map_moisture_range_to_led(sensor_value)

    index = min(index, len(led_array) - 1)

    # Handle the case when the moisture reading is 10 or below (all LEDs should be off)
    if sensor_value <= 10:
        for i in range(len(led_array)):
            led_array[i].off()
    else:
        # Handle the case when the index is 0 (turn off all except the first LED)
        if index == 0:
            for i in range(1, len(led_array)):
                led_array[i].off()
            led_array[0].on()
        else:
            # Turn off LEDs from the index + 1 to the end to represent values below the sensor value
            for i in range(index + 1, len(led_array)):
                led_array[i].off()

            # Turn on LEDs up to the index to represent the sensor value
            for i in range(index + 1):
                led_array[i].on()

def run():
    while True:
        water_reading = water.get_capacitor_measurements()
        moisture_level = map_moisture_range_to_led(water_reading)
        display_bar_graph(moisture_level)
        utime.sleep(.1)

