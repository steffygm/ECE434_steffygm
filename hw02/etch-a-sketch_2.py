#!/usr/bin/env python3


import Adafruit_BBIO.GPIO as GPIO
import time
import curses


width = 50
height = 25

x = int(width/2)
y = int(height/2)

grid = []

for i in range(width):
    grid.append([])
    for j in range(height):
        grid[i].append("#")

def pbar(window):
    global x
    global y
    while 1:
        for x_out in range(width):
            for y_out in range(height):
                window.addstr(1+y_out, 1+x_out, grid[x_out][y_out])
            window.addstr("\n")
        window.refresh()
        time.sleep(0.05)

BUTTON_R = "P9_21"
BUTTON_G = "P9_22"
BUTTON_Y = "P9_23"
BUTTON_B = "P9_24"

GPIO.setup(BUTTON_R, GPIO.IN)
GPIO.setup(BUTTON_G, GPIO.IN)
GPIO.setup(BUTTON_Y, GPIO.IN)
GPIO.setup(BUTTON_B, GPIO.IN)

def updatePOS(channel):
    global x
    global y
    global grid
    state = GPIO.input(channel)
    if(state == 1):
        if(channel == BUTTON_R):
            x-=1
        if(channel == BUTTON_G):
            y-=1
        if(channel == BUTTON_Y):
            y+=1
        if(channel == BUTTON_B):
            x+=1
        if x == 0:
            x = width -1
        if x == width:
            x = 0
        if y == 0:
            x = height -1
        if y == height:
            y = 0
        grid[x][y] = " "

GPIO.add_event_detect(BUTTON_R, GPIO.BOTH, callback=updatePOS)
GPIO.add_event_detect(BUTTON_G, GPIO.BOTH, callback=updatePOS)
GPIO.add_event_detect(BUTTON_Y, GPIO.BOTH, callback=updatePOS)
GPIO.add_event_detect(BUTTON_B, GPIO.BOTH, callback=updatePOS)

try:
    curses.wrapper(pbar)
except KeyboardInterrupt:
    print("\nCleaning Up")
    GPIO.cleanup()
GPIO.cleanup()