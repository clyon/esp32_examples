from machine import Pin, SPI
import time

class MAX6675:
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs

    def read_temp(self):
        self.cs.off()
        time.sleep_us(100)
        data = self.spi.read(2)
        self.cs.on()
        value = (data[0] << 8) | data[1]
        if value & 0x4:
            return None  # open circuit
        temp = ((value >> 3) & 0xfff) * 0.25
        return temp

# setup SPI
spi = SPI(1, baudrate=1000000, polarity=0, phase=0)

# setup chip select
cs = Pin(15, Pin.OUT)
cs.on()

# setup MAX6675
max6675 = MAX6675(spi, cs)

while True:
    temp = max6675.read_temp()
    if temp is not None:
        print('Temperature: {:.2f}C'.format(temp))
    else:
        print('Error: Open circuit')
    time.sleep(1)

