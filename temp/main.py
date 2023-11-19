from machine import ADC, Pin
import math

# Constants for the Steinhart-Hart equation - these need to be calibrated for your specific thermistor
A = 1.009249522e-03
B = 2.378405444e-04
C = 2.019202697e-07

# Setup ADC for ESP32
adc = ADC(Pin(5))  # Use the correct pin for your setup
adc.atten(ADC.ATTN_11DB)  # Configure the attenuation for the full range of the ADC

def read_temperature():
    # Read the ADC value
    adc_value = adc.read()

    # Convert ADC value to resistance
    # This depends on the voltage divider configuration
    # Example: If using a 10k resistor in series with the thermistor
    resistance = 10000 / ((4095 / adc_value) - 1) 

    # Calculate temperature using the Steinhart-Hart equation
    ln_resistance = math.log(resistance)
    temperature = 1 / (A + B * ln_resistance + C * ln_resistance ** 3)

    # Convert from Kelvin to Celsius. 
    temperature_celsius = temperature - 273.15

    return temperature_celsius

# Main loop
while True:
    temperature = read_temperature()
    print("Temperature: {:.2f} C".format(temperature))
    time.sleep(1)
