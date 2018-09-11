#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time
import sys

LED_R = "P9_25"
delay = float(sys.argv[1])

GPIO.setup(LED_R, GPIO.OUT)
GPIO.output(LED_R, 1)
try:
    while True:
        GPIO.output(LED_R, 0)
        time.sleep(delay)
        GPIO.output(LED_R, 1)
        time.sleep(delay)
except KeyboardInterrupt:
    print("\nCleaning Up")
    GPIO.cleanup()
GPIO.cleanup()