CC= gcc
CFLAGS= -O3 -g
#
# Programs
#
all: button_2_led_mmap fast_led_mmap
	./configure_pins

button_2_led_mmap: button_2_led_mmap.c beaglebone_gpio.h
	$(CC) $(CFLAGS) -o $@ $<

fast_led_mmap:  fast_led_mmap.c beaglebone_gpio.h
    $(CC) $(CFLAGS) -o $@ $<

#
# Objects
#

%.o: %.c
    $(CC) $(CFLAGS) $(TOOLS_CFLAGS) -c $< -o $@

clean:
    rm button_2_led_mmap fast_led_mmap

print:
    @echo LDFLAGS = $(LDFLAGS)
