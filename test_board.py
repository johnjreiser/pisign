import board
import neopixel
import time
p = neopixel.NeoPixel(board.D18, 256)

from matrix import LedMatrix
a = LedMatrix().ledarray()

from colorsys import hsv_to_rgb

for row in range(0,8):
    for column in range(0,32):
        p[ int(a[row][column]) ] = [int(x*64) for x in hsv_to_rgb( row/8, 1, 1 ) ]

