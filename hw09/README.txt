Griffin Steffy
hw09
ECE434-01

NOTE: I will get the other oscilliscope captures on Tuesday (10/23) if it is not already graded

2.6 Blinking an LED
	- cd part2.6
	- run "source ./setup.sh" to configure pins
	- use the makefile to compile and run the code to make the LED blink
	- it can't be read without an oscilliscope because of the speed
5.3 PWM Generator
	- run "source ./pwm1_setup.sh"
	- run "make" to run code pwm1.c
5.4 Controlling the PWM Frequency
	- run "source ./pwm4_setup.sh"
	- run "make" to run code pwm4.c
5.5 Loop Unrolling for Better Performance
	- run "source ./pwm5_setup.sh"
	- run "make" to run code pwm5.c
5.9 Reading an Input at Regular Intervals
	- run "source ./input_setup.sh"
	- run "make" to run code input1.c

5.10 Analog Wave Generator

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Table~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Part      Speed      Jitter?      Stable?             StdDev?     PNG
2.6       12.5Mhz    Yes          Yes (consistent)    N/A         part2.6.png
|         |          |            |                   |           |
5.3       N/A        Yes          Yes (consistent)    N/A         part5.3_1.png & part5.3_2.png
|         |          |            |                   |           |
5.4       N/A        < 5.3's      Yes (less than 5.3) N/A         part5.4.png
|         |          |            |                   |           |
5.5       N/A        Yes          Yes (less than 5.4) N/A         part5.5.png
|         |          |            |                   |           |
5.9       us range   N/A          N/A                 N/A         N/A
          (forgot to save oscilliscope reading)       |           |
|         |          |            |                   |           |
5.10      |          |            |                   |           | 
|         |          |            |                   |           |
