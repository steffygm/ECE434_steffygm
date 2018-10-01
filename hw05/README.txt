Griffin Steffy
ECE434 - 01 : Professor Yoder
Homework #5

Make
    1) be in the hw05 directory (make it currend directory) in terminal ON THE BONE
    2) enter make into terminal
        - this should compile and create an app.o, and app.arm file
        - the .arm file is an executable and can be ran
    3) Make clean to remove files created by makefile

Installing the Kernel Source
    - I installed the kernel on my host computer

Cross-Compiling
    I pasted the outputs of the cross-compile exercise below:

    Output from Host:
    griffin@Linux-VM:/media/sf_ECE434/exercises$ ./a.out 
    Hello, World! Main is executing at 0x561207cb26aa
    This address (0x7ffea4c4a070) is in our stack frame
    This address (0x561207eb3018) is in our bss section
    This address (0x561207eb3010) is in our data section

    Output from Bone:
    griffin@Linux-VM:~/Documents/bb-kernel/dl$ ssh bone ./a.out
    Warning: Permanently added 'bone,192.168.7.2' (ECDSA) to the list of known hosts.
    Hello, World! Main is executing at 0x103d5
    This address (0xbef19c54) is in our stack frame
    This address (0x20668) is in our bss section
    This address (0x20660) is in our data section

Kernel Modules
    - I did the exercises, but I am confused on what files you would like to see to prove that I completed them.
        I pasted a one of the final outputs from the kernel moduels below.

        debian@beaglebone:~/exploringBB/extras/kernel/ebbchar$ sudo ./test 
        Starting device test code example...
        Type in a short string to send to the kernel module:
        Rose-Hulman
        Writing message to the device [Rose-Hulman].
        Press ENTER to read back from the device...

        Reading from the device...
        The received message is: [Rose-Hulman]
        End of the program
        debian@beaglebone:~/exploringBB/extras/kernel/ebbchar$ dmesg -H | tail -8
        [Oct 1 05:11] EBBChar: Initializing the EBBChar LKM
        [  +0.000038] EBBChar: registered correctly with major number 241
        [  +0.000118] EBBChar: device class registered correctly
        [  +0.000314] EBBChar: device class created correctly
        [ +28.228291] EBBChar: Device has been opened 1 time(s)
        [Oct 1 05:12] EBBChar: Received 11 characters from the user
        [  +2.422633] EBBChar: Sent 11 characters to the user
        [  +0.000643] EBBChar: Device successfully closed

    - I did the exercise to copy P9_15 to P9_16.
    - When I toggled the pin (As fast as Possible) I got a period of around 150 us.
        The CPU Usage was much lower than the previous times when we did a similar program.

