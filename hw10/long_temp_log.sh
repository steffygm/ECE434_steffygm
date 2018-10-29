#!/bin/bash
t=0
while [ $t -le 15 ]
do
./temp_sheet.sh
sleep 5m
t=$(( $t + 1 ))
done
