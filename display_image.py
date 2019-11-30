import board
import neopixel
import time
p = neopixel.NeoPixel(board.D18, 256, bpp=3, brightness=.5, auto_write=False)

from matrix import LedMatrix
a = LedMatrix().ledarray()

from PIL import Image
from io import BytesIO
import sys, requests

def halfC(t):
    array = []
    for i in t:
        array.append(int(i/2.0))
    return array

if len(sys.argv) > 1:
    url = sys.argv[1]
    if url[:4] == 'http':
        srcimg = requests.get(url).content
        img = Image.open(BytesIO(srcimg))
    else: 
        srcimg = open(url, 'rb')
        img = Image.open(srcimg)
else:
    raise Exception("Must specify URL")
    sys.exit(2)

resized = img.resize( (32,8) ).convert('RGB')

for row in range(0,8):
    for col in range(0,32):
        p[ a[row][col] ] = halfC( resized.getpixel( (col,row) ) )
p.show()

