import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)
pixels[0] = (55, 55, 0)