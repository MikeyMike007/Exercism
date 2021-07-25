#include "resistor_color.h"
#include <stdlib.h>

enum { nr_colors = 10 };

// Returns the color (number) of the variable color
int color_code(resistor_band_t color) {
    return color;
}

// Return a pointer to the local array allColors so it can be retrieved
// in the test fil,
const resistor_band_t* colors(void) {
    /*resistor_band_t *allColors = malloc(nr_colors * sizeof(int));*/
    static resistor_band_t all_colors[nr_colors];
    for (resistor_band_t color = BLACK; color <= WHITE; color++) {
        all_colors[color] = color;
    }
    return all_colors;
}

