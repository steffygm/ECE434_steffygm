#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2
import time
import curses

# Width/Height complete
width = 50
height = 25

# Initialize position to center
x = int(width/2)
y = int(height/2)

# Declare grid array
grid = []

# Initalize Grid values
for i in range(width):
    grid.append([])
    for j in range(height):
        grid[i].append("#")

# Update Grid Display
def grid_display(window):
    global x
    global y
    global grid
    while 1:
        for x_out in range(width):
            for y_out in range(height):
                window.addstr(1+y_out, 1+x_out, grid[x_out][y_out])
            window.addstr("\n")
        window.refresh()
        time.sleep(0.05)

# Update Position and Grid Values
def updatePOS(channel):
    global x
    global y
    global grid
    state = GPIO.input(channel)
    if(state == 1):
        if(channel == BUTTON_X):
            for i in range(width):
                for j in range(height):
                    grid[i][j] = "#"
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

# Instantiate the class to access channel eQEP2, and initialize
# that channel
r_Encoder = RotaryEncoder(eQEP2)
r_Encoder.setAbsolute()
r_Encoder.enable()

# Initalize Encoder Position
r_pos = r_Encoder.position
new_r_pos = r_pos

# Busy loop & draw grid to screen
try:
    curses.wrapper(grid_display)
    new_r_pos = r_Encoder.position
    if(new_r_pos < r_pos):
        x-=1
    elif(new_r_pos > r_pos):
        x+=1
    r_pos = new_r_pos
    grid[x][y] = " "
except KeyboardInterrupt:
    print("\nCleaning Up")
    GPIO.cleanup()
GPIO.cleanup()