from machine import Pin, SPI
import time

# Initialize SPI
# Replace 'sck', 'mosi', 'miso' with the actual GPIO pins you are using
spi = SPI(1, baudrate=9600, polarity=0, phase=0, sck=Pin(5), mosi=Pin(22), miso=Pin(19))

# Chip Select pin
cs = Pin(23, Pin.OUT)
cs.value(1)  # Set CS high to start with

def read_temp():
    cs.value(0)  # Set CS low to start the transaction
    data = spi.read(2)  # Read 2 bytes of data
    cs.value(1)  # Set CS high to end the transaction

    # Convert the data to temperature
    value = (data[0] << 8) | data[1]
    if (value & 0x4):
        # No thermocouple attached
        return None
    else:
        # Calculate the temperature
        return (value >> 3) * 0.25

while True:
    temperature = read_temp()
    if temperature is not None:
        temperature = temperature * 1.8 + 32
        print("Temperature:", temperature, "°F")
    else:
        print("No thermocouple attached")
    time.sleep(2)