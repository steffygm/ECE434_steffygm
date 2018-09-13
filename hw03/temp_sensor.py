#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

bus = smbus.SMBus(2)
tmp101_1 = 0x49
tmp101_2 = 0x48
matrix = 0x70

hot  = [0x00, 0xFF, 
        0x00, 0xFF, 
        0x00, 0xFF, 
        0x00, 0xFF,
        0x00, 0xFF, 
        0x00, 0xFF, 
        0x00, 0xFF, 
        0x00, 0xFF]

perf = [0xFF, 0xFF, 
        0xFF, 0xFF, 
        0xFF, 0xFF, 
        0xFF, 0xFF, 
        0xFF, 0xFF, 
        0xFF, 0xFF, 
        0xFF, 0xFF, 
        0xFF, 0xFF]

cold = [0xFF, 0x00, 
        0xFF, 0x00, 
        0xFF, 0x00, 
        0xFF, 0x00, 
        0xFF, 0x00, 
        0xFF, 0x00, 
        0xFF, 0x00, 
        0xFF, 0x00]

off  = [0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00]

# LED Matrix Setup
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

bus.write_i2c_block_data(matrix, 0, hot) 
time.sleep(1)  
try:
    while True:
        temp1 = bus.read_byte_data(tmp101_1, 0)
        temp2 = bus.read_byte_data(tmp101_2, 0)
        print ("Temp1: " + str(temp1), end=" ")
        print ("Temp2: " + str(temp2), end="\r")
        if(temp2 > temp1):
            bus.write_i2c_block_data(matrix, 0, hot)
        elif(temp2 == temp1):
            bus.write_i2c_block_data(matrix, 0, perf)
        else:
            bus.write_i2c_block_data(matrix, 0, cold)

        time.sleep(0.25)
except KeyboardInterrupt:
    print("\nCleaning Up")
    bus.write_i2c_block_data(matrix, 0, off)
    GPIO.cleanup()
GPIO.cleanup()
