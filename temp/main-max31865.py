from machine import Pin, SPI
import time

# Configure the SPI bus
spi = SPI(1, baudrate=1000000, polarity=0, phase=1, sck=Pin(5), mosi=Pin(22), miso=Pin(19))

# CS pin setup for MAX31865
cs = Pin(23, Pin.OUT)

def read_temperature(cs):
    # Read data from MAX31865
    cs.value(0)
    data = spi.read(8)  # Read 8 bytes of data
    cs.value(1)

    # Convert the data to temperature
    # Assuming a PT100 sensor here
    resistance = ((data[1] << 8) | data[2]) >> 1
    temperature = resistance_to_temperature(resistance)

    return temperature

def resistance_to_temperature(resistance):
    # Convert resistance to temperature
    # This is a simple linear approximation, you might need a more accurate method
    temperature = (resistance - 19182.59) / 110.58
    #temperature = resistance
    return temperature

# Main loop
while True:
    temp = read_temperature(cs)
    print("Temperature: {:.2f} C".format(temp))
    tempc = temp * 1.8 + 32
    print("Temperature: {:.2f} F".format(tempc))
    time.sleep(1)
