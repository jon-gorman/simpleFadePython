import time
import board
import neopixel

pixel_pin = board.A1
num_pixels = 12
brightness = 0

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

def redin():
    for i in range(0, 10, 1):
        pixels.fill((255, 0, 0))
        pixels.brightness = i


def greenin():
    for i in range(0, 255, 2):
        pixels.fill((0, i, 0))
def greenout():
    for i in range(255, 0, -2):
        pixels.fill((0, i, 0))


def bluein():
    for j in range(0, 255, 2):
        pixels.fill((0, 0, j))


def blueout():
    for i in range(255, 0, -2):
        pixels.fill((0, 0, i))


while True:
    # time.sleep(.5)
    # redin()
    time.sleep(.05)
    bluein()
    time.sleep(.05)
    blueout()
    time.sleep(.05)
    greenin()
    time.sleep(.05)
    greenout()

