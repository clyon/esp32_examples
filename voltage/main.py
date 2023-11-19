from machine import ADC, Pin
import time

# Initialize ADC
adc = ADC(Pin(25))  # change the Pin number based on your hardware setup
adc.atten(ADC.ATTN_11DB)  # configure the attenuation for full range

# Constants for battery voltage range
FULL_CHARGE_VOLTAGE = 4.2  # maximum voltage when fully charged
CUT_OFF_VOLTAGE = 3.0  # minimum operational voltage

def read_battery_voltage():
    # Read raw ADC value
    raw_value = adc.read()
    
    # Convert raw ADC value to voltage
    # This conversion depends on your ADC resolution and reference voltage
    # For example, for a 12-bit ADC with 3.3V reference:
    voltage = raw_value / 1845 * 3.3
    print(f"Raw Value: {raw_value:.4f}V")
    return voltage

def battery_percentage(voltage):
    # Calculate percentage based on voltage range
    percentage = (voltage - CUT_OFF_VOLTAGE) / (FULL_CHARGE_VOLTAGE - CUT_OFF_VOLTAGE) * 100

    # Clamp percentage to 0-100%
    percentage = max(0, min(100, percentage))

    return percentage

while True:
    voltage = read_battery_voltage()
    percent = battery_percentage(voltage)
    print(f"Battery Voltage: {voltage:.2f}V, Capacity: {percent:.0f}%")
    time.sleep(1)