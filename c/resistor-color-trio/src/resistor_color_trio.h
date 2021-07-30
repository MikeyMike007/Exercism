#ifndef RESISTOR_COLOR_TRIO_H
#define RESISTOR_COLOR_TRIO_H

#include <stdint.h>

typedef enum {
    BLACK,
    BROWN,
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    VIOLET,
    GREY,
    WHITE
} resistor_band_t;

typedef enum {
    OHMS,
    KILOOHMS
} units;

typedef struct {
    uint16_t value;
    units units;
} resistor_value_t;

// Function attributes
uint16_t color_code(resistor_band_t colors[]);

#endif
