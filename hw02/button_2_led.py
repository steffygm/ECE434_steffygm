#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

# Pin Declaratoin
LED_R = "P9_25"
LED_G = "P9_26"
LED_Y = "P9_27"
LED_B = "P9_28"
BUTTON_R = "P9_21"
BUTTON_G = "P9_22"
BUTTON_Y = "P9_23"
BUTTON_B = "P9_24"

# GPIO Pin Setup
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
GPIO.setup(BUTTON_R, GPIO.IN)
GPIO.setup(BUTTON_G, GPIO.IN)
GPIO.setup(BUTTON_Y, GPIO.IN)
GPIO.setup(BUTTON_B, GPIO.IN)

# Pin Initialization
GPIO.output(LED_R, 1)
GPIO.output(LED_G, 1)
GPIO.output(LED_Y, 1)
GPIO.output(LED_B, 1)

# Button to LED map
map = {BUTTON_R: LED_R, BUTTON_G: LED_G, BUTTON_Y: LED_Y, BUTTON_B: LED_B}

# Button Interrupt
def updateLED(channel):
    state = GPIO.input(channel)
    GPIO.output(map[channel], 1 - state)
    if(state == 1):
        if(channel == BUTTON_R):
            print("Red")
        if(channel == BUTTON_G):
            print("Green")
        if(channel == BUTTON_Y):
            print("Yellow")
        if(channel == BUTTON_B):
            print("Blue")

# Button Interrupt Assign
GPIO.add_event_detect(BUTTON_R, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(BUTTON_G, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(BUTTON_Y, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(BUTTON_B, GPIO.BOTH, callback=updateLED)

# Busy Loop and exit strategy
try:
    while True:
            time.sleep(100)
except KeyboardInterrupt:
    print("\nCleaning Up")
    GPIO.cleanup()
GPIO.cleanup()