import time
import board
import neopixel

LED_COUNT = 135

#                 	         PIN
pixels = neopixel.NeoPixel(board.D18, LED_COUNT)
pixels.fill((0,0,0))

for x in range(LED_COUNT):
    pixels[x] = (0, 255, 255)
    time.sleep(0.25)

for x in range(LED_COUNT):
    pixels[x] = (0, 0, 0)
    time.sleep(0.25)
