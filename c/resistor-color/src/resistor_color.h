#ifndef RESISTOR_COLOR_H
#define RESISTOR_COLOR_H

// Variable attribute of type enum / resistor_band_t
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

// Function attributes
int color_code(resistor_band_t color);
const resistor_band_t* colors(void);

#endif
