#!/bin/bash
temp_C=$(i2cget -y 2 0x48)
temp_F=$(($temp_C *9/5 + 32))
echo "The Temperature is: $temp_F degrees F"