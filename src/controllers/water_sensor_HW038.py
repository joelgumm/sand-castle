from machine import ADC, Pin
import utime


def get_capacitor_measurements():
    soil_adc = ADC(Pin(26))
    return soil_adc.read_u16()
