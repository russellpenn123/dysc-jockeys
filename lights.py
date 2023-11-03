import board
import neopixel

#                 	    PIN     LED Count
pixels = neopixel.NeoPixel(board.D18, 60)
pixels.fill((0,255,0))
