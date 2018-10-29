#!/bin/bash
config-pin P9_17 i2c
config-pin P9_18 i2c
temp_C=$(i2cget -y 1 0x49)
temp_F=$(($temp_C *9/5 + 32))
echo "The Temperature is: $temp_F degrees F"
./demo.py $temp_F $temp_F
