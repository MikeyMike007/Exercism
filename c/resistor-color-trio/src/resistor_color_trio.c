#include "resistor_color_trio.h"
#include <stdint.h>
#include <stdio.h>

uint16_t color_code(resistor_band_t colors[]) {
    int result = 0;
    int factor = 10;
    int nr_colors = 0;

    while (*colors) {
        nr_colors++;
        printf("%d\n", nr_colors);
        ++colors;
    }


    return 0;
}


int main() {
    int test = color_code((resistor_band_t[]){BLUE, GREY, BROWN});
    return 0;
}
