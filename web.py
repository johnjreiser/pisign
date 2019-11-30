from flask import Flask, jsonify, render_template
import board
import neopixel
from colorsys import hsv_to_rgb
from matrix import LedMatrix

p = neopixel.NeoPixel(board.D18, 256, bpp=3, brightness=.25, auto_write=False)
a = LedMatrix().ledarray()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", matrix=a)

@app.route("/pixel/<int:pix>/<color>")
def pixel(pix,color=None):
    if color:
        rgbc = tuple(int(color.lstrip("#")[i:i+2], 16) for i in (0,2,4))
    else:
        rgbc = (0,0,0)
    p[ pix ] = rgbc
    p.write()
    return jsonify({'pix':pix,'color':rgbc})

@app.route("/pixels")
def pixels():
    return jsonify([ "{0:02x}{1:02x}{2:02x}".format(*x) for x in p ])

@app.route("/fill/<color>")
def clear(color=None):
    if color:
        rgbc = tuple(int(color.lstrip("#")[i:i+2], 16) for i in (0,2,4))
    else:
        rgbc = (0,0,0)
    p.fill(rgbc)
    p.write()
    return jsonify({});

@app.route("/rainbow")
def rainbow():
    for row in range(0,8):
        for column in range(0,32):
            p[ int(a[row][column]) ] = [ int(x*255) for x in hsv_to_rgb( row/8, 1, 1 ) ]
    p.write()
    return jsonify({});

if __name__ == '__main__':
    app.run("0.0.0.0", "80")
