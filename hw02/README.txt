Pin configuration
Buttons: 
    - Red : P9_21
    - Green : P9_22
    - Yellow : P9_23
    - Blue : P9_24
    - Clear (X) : P9_17
Leds:
    - Red : P9_25
    - Green : P9_26
    - Yellow : P9_27
    - Blue : P9_28

Buttons and LEDs
    File: button_2_led.py
        run this python code on the bone, each button corresponds to an individual LEDs
Measuring a gpio pin on an Oscilloscope

Measuring a gpio pin on an Oscilloscope
    Files: togglegpio.py, togglegpio.sh (exercises/gpio - given), blinkLED.code
    for the python, c, input the delay (in seconds) and an led linked to GPIO 117 will blink with that delay
    compile the c like this: (gcc –lsoc -o blinkLED blinkLED.c)

Etch-a-sketch
    File: etch-a-sketch_2.py
    this file runs in the terminal on the BB, displays a grid that is 50x25 and the game is controlled by 4 direction buttons and a reset button

Oscilliscope Results
    File: hw02_table.xlsx
    this file contains the results from each question for each script technique as well as a chart for specific input values and the output period. 
