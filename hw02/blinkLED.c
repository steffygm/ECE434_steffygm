#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdint.h>

#include <libsoc_gpio.h>
#include <libsoc_debug.h>

#define GPIO_OUTPUT 117 

int main(int argc, char* argv[]) {
  if (argc < 2)
  {
        printf("Missing input arguments\n");
  }
  uint16_t delay = atoi(argv[1]);
  gpio *gpio_output;    // Create gpio pointer
  libsoc_set_debug(1);  // Enable debug output
  // Request gpio
  gpio_output = libsoc_gpio_request(GPIO_OUTPUT, LS_GPIO_SHARED);
  // Set direction to OUTPUT
  libsoc_gpio_set_direction(gpio_output, OUTPUT);

  libsoc_set_debug(0);   // Turn off debug printing for fast toggle

  int i;
  for (i=0; i<10000; i++) {     // Toggle the GPIO 100 times
    libsoc_gpio_set_level(gpio_output, HIGH);
    usleep(delay);           // sleep 100,000 uS
    libsoc_gpio_set_level(gpio_output, LOW);
    usleep(delay);
  }

  if (gpio_output) {
    libsoc_gpio_free(gpio_output);  // Free gpio request memory
  }

  return EXIT_SUCCESS;
}
