#!/usr/bin/env python3
import smbus
import time
import Adafruit_BBIO.GPIO as GPIO
import time

# LED Matrix Setup
bus = smbus.SMBus(2) # Use i2c bus 1
# Matrix address
matrix = 0x70
# The first byte is GREEN, the second is RED.
#   [GREEN0, RED0, GREEN1, RED1, ...GREEN7, RED7]
smile = [0x00, 0x3c, 0x00, 0x42, 0x28, 0x89, 0x04, 0x85,
0x04, 0x85, 0x28, 0x89, 0x00, 0x42, 0x00, 0x3c]

# LED Declaration
LED_R = "P9_25"
LED_G = "P9_26"
LED_Y = "P9_27"
LED_B = "P9_28"

# Button Declaration
BUTTON_R = "P9_21"
BUTTON_G = "P9_22"
BUTTON_Y = "P9_23"
BUTTON_B = "P9_24"

# Global Var Declaration
delay = 0.25

# GPIO Setup
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
GPIO.setup(BUTTON_R, GPIO.IN)
GPIO.setup(BUTTON_G, GPIO.IN)
GPIO.setup(BUTTON_Y, GPIO.IN)
GPIO.setup(BUTTON_B, GPIO.IN)

# GPIO Initalization
GPIO.output(LED_R, 1)
GPIO.output(LED_G, 1)
GPIO.output(LED_Y, 1)
GPIO.output(LED_B, 1)

map = {BUTTON_R: LED_R, BUTTON_G: LED_G, BUTTON_Y: LED_Y, BUTTON_B: LED_B}

# Button Detect
def updateLED(channel):
    state = GPIO.input(channel)
    GPIO.output(map[channel], 1 - state)
    if(state == 1):
        if(channel == BUTTON_R):
            # print("Red")
        if(channel == BUTTON_G):
            # print("Green")
        if(channel == BUTTON_Y):
            # print("Yellow")
        if(channel == BUTTON_B):
            # print("Blue")

# Button Event Assignment
GPIO.add_event_detect(BUTTON_R, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(BUTTON_G, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(BUTTON_Y, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(BUTTON_B, GPIO.BOTH, callback=updateLED)

# LED Matrix Setup
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

# LED Matrix Write
bus.write_i2c_block_data(matrix, 0, smile)
time.sleep(delay)

try:
    while True:
            time.sleep(100)
except KeyboardInterrupt:
    print("\nCleaning Up")
    GPIO.cleanup()
GPIO.cleanup()