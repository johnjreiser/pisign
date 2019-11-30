import board
import neopixel
import time
p = neopixel.NeoPixel(board.D18, 256, bpp=3, brightness=.5, auto_write=False)

from matrix import LedMatrix
a = LedMatrix().ledarray()

from colorsys import hsv_to_rgb

for row in range(0,8):
    for column in range(0,32):
        p[ int(a[row][column]) ] = [ int(x*255) for x in hsv_to_rgb( row/8, 1, 1 ) ]

try:
    while True:
        a = a[1:] + a[:1]
        for row in range(0,8):
            for column in range(0,32):
                p[ int(a[row][column]) ] = [ int(x*255) for x in hsv_to_rgb( row/8, 1, 1 ) ]
        p.show()
        time.sleep(.01)
except KeyboardInterrupt:
    pass
finally:
    p.fill( ( 0,0,0 ) )
    p.show()
