#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import time
import smbus

# i2c setup
bus = smbus.SMBus(2) # Use i2c bus 2
tmp101_2 = 0x48      # tmp101 at address 0x48
matrix = 0x70        # LED Matrix address 0x70

# LED Matrix Setup
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

# Grid setup
width = 7   # 8-1
height = 7  # 8-1

x = 3
y = 3

# Rotary Encoder Setup
# eQEP2 - config-pin P8_41 qep
# eQEP2 - config-pin P8_42 qep
#
# eQEP1 - config-pin P8_33 qep
# eQEP1 - config-pin P8_35 qep
l_Encoder = RotaryEncoder(eQEP2)
l_Encoder.setAbsolute()
l_Encoder.enable()

r_Encoder = RotaryEncoder(eQEP1)
r_Encoder.setAbsolute()
r_Encoder.enable()


# Initalize Encoder Position
r_pos = r_Encoder.position
l_pos = l_Encoder.position
new_r_pos = r_pos
new_l_pos = l_pos

# Initial Temp reading
temp_init = bus.read_byte_data(tmp101_2, 0)

# Matrix Initalization
# Left starts at top
# Top Starts at left
leds  = [0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00]

# Empty Array for matrix manipulation
empty  = [0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00]

# Inital Write to LED Matrix
bus.write_i2c_block_data(matrix, 0, leds)

# Main Loop
try:
    while True:
        new_r_pos = r_Encoder.position
        new_l_pos = l_Encoder.position

        # Update X Position
        if(new_r_pos < r_pos):
            x+=1
        elif(new_r_pos > r_pos):
            x-=1
        if(x > width):
            x = 0
        elif(x < 0):
            x = width

        # Update y position
        if(new_l_pos < l_pos):
            y+=1
        elif(new_l_pos > l_pos):
            y-=1
        if(y > height):
            y = 0
        elif(y < 0):
            y = height
        r_pos = new_r_pos
        l_pos = new_l_pos
        
        # Update Graphic to new position, and write to matrix
        leds[2*x] = leds[2*x]|(0x80>>y)
        bus.write_i2c_block_data(matrix, 0, leds)

        # Check if Display must be cleared
        temp = bus.read_byte_data(tmp101_2, 0)
        print ("Temp: " + str(temp), end="\r")
        if(temp > temp_init+2):
            for i in range(0, 15):
                leds[i] = 0x00

        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nCleaning Up")
    bus.write_i2c_block_data(matrix, 0, empty)
    GPIO.cleanup()
GPIO.cleanup()