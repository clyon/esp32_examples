from machine import ADC, Pin
import time

# Initialize ADC
adc_pin = 34  # Replace with your ADC pin number
adc = ADC(Pin(adc_pin))

# Configure ADC resolution
adc.width(ADC.WIDTH_12BIT)  # 12-bit resolution

# Function to read voltage
def read_voltage(adc, reference_voltage=3.3):
    value = adc.read()
    print ("Raw Value:", value)
    voltage = value / 4095 * reference_voltage
    return voltage

# Main loop
while True:
    voltage = read_voltage(adc)
    print("Voltage:", voltage, "V")

    # Delay for a second
    time.sleep(1)
