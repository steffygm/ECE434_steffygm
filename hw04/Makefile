TOOLS_CFLAGS    := -Wstrict-prototypes -Wshadow -Wpointer-arith -Wcast-qual \
                   -Wcast-align -Wwrite-strings -Wnested-externs -Winline \
                   -W -Wundef -Wmissing-prototypes
CFLAGS  := -O3 -g
#
# Programs
#
all:    gpioThru gpioToggle

button_2_led_mmap: button_2_led_mmap.c beaglebone_gpio.h
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

fast_led_mmap:  fast_led_mmap.c beaglebone_gpio.h
    $(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

#
# Objects
#

%.o: %.c
    $(CC) $(CFLAGS) $(TOOLS_CFLAGS) -c $< -o $@

clean:
    rm button_2_led_mmap fast_led_mmap

print:
    @echo LDFLAGS = $(LDFLAGS)
