#include "darts.h"
#include <math.h>

uint8_t score(coordinate_t my_position) {
    float my_radius = radius(my_position);

    if (my_radius <= RADIUS_MAX_SCORE)
        return MAX_SCORE;
    else if (my_radius > RADIUS_MAX_SCORE && my_radius <= RADIUS_MIDDLE_SCORE)
        return MIDDLE_SCORE;
    else if (my_radius > RADIUS_MIDDLE_SCORE && my_radius <= RADIUS_LOW_SCORE)
        return LOW_SCORE;

    return NO_SCORE;
}

float radius(coordinate_t landing_position) {
    return sqrt(pow(landing_position.x, 2) + pow(landing_position.y, 2));

}
