#include "resistor_color_duo.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int color_code(resistor_band_t* colors) {
    char* encoded_number = (char* )malloc(NR_COLORS * sizeof(char));
    char* color_band = (char *)malloc(sizeof(char));

    for (int i = 0; i < NR_COLORS; i++) {
        // Why does the commented code not work below?
        // char* color_band = (char* )malloc(sizeof(char));
        resistor_band_t color = colors[i];
        sprintf(color_band, "%d", color);
        strcat(encoded_number, color_band);
        //free(color_band);
    }
    return atoi(encoded_number);
}
