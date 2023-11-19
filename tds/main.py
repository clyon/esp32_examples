from machine import ADC, Pin
import time

# Initialize ADC
adc = ADC(Pin(32))  # Change the pin number based on your connection
adc.atten(ADC.ATTN_11DB)  # Set the attenuation for full range of sensor

def read_tds():
    # Read the analog value
    analog_value = adc.read()
    
    # Convert the analog value to TDS value
    # The conversion depends on the specific sensor and its calibration.
    # The following is a generic formula and might need adjustment.
    tds_value = analog_value * (3.3 / 4096) * 1000
    return tds_value

while True:
    tds = read_tds()
    print("TDS Value:", tds, "ppm")
    time.sleep(2)

