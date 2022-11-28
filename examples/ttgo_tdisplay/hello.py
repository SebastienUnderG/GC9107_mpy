"""
hello.py

    Writes "Hello!" in random colors at random locations on a
    LILYGO® TTGO T-Display.

    https://www.youtube.com/watch?v=atBa0BYPAAc

"""
import random
from machine import Pin, SoftSPI, SPI
import st7789py as st7789

# Choose a font

from romfonts import vga1_8x8 as font
# from romfonts import vga2_8x8 as font
# from romfonts import vga1_8x16 as font
# from romfonts import vga2_8x16 as font
# from romfonts import vga1_16x16 as font
# from romfonts import vga1_bold_16x16 as font
# from romfonts import vga2_16x16 as font
# from romfonts import vga2_bold_16x16 as font
# from romfonts import vga1_16x32 as font
# from romfonts import vga1_bold_16x32 as font
# from romfonts import vga2_16x32 as font
# from romfonts import vga2_bold_16x32 as font


def main():
    spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(15))

    tft = st7789.ST7789(
        spi,
        128,
        128,
        reset=Pin(7, Pin.OUT),
        cs=Pin(17, Pin.OUT),
        dc=Pin(6, Pin.OUT),
        rotation=0)

    while True:
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(0)
            col_max = tft.width - font.WIDTH*6
            row_max = tft.height - font.HEIGHT

            for _ in range(100):
                tft.text(
                    font,
                    "Hello!",
                    random.randint(0, col_max),
                    random.randint(0, row_max),
                    st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)),
                    st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8))
                )


main()
