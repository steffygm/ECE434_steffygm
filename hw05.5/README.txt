Griffin Steffy
hw06
ECE434-01 : Professor Yoder

Questions:

1) Where does Julia Cartwrige work?
    National Instruments

2) What is PREEMT_RT?
    Real Time Linux Kernel Patch

3) What is mixed criticality?
    The mix of time intensive tasks, and non time intensive tasks running together and communicate

4) How can drivers misbehave?
    shared kernel, scheduler, stack between RT tasks and non-RT tasks

5) What is the delta in Figure 1?
    latency is the delta between the event and the application launch

6) What is Cyclictest [2]?
    take a timestamp, sleep for set duration, then take another time stamp
    the difference between the two timestamps is the actual time slept
    subtract the set duration from this to find the latency

7) What is plotted in Figure 2?
    two results of the Cyclictest using preempt and preempt_rt

8) What is dispatch latency? Scheduling latency?
    dispatch latency - difference between hardware firing and thread scheduler being told what thread to running
    scheduling latency - difference between scheduler knowing what thread to run and the thread actually being run

9) What is mainline?
    the single process that is running, which could contain multiple threads being switched on and off of the process

10) What is keeping the External event in Figure 3 from starting?
    It can't be scheduled until the lower priority thread (interrupt) finishes

11) Why can the External event in Figure 4 start sooner?
    it is now preemptive, because the irq interrupt goes to a small temporary thread that allows higher priority, tasks to be placed on the process over smaller priority threads