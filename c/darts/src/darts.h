#ifndef DARTS_H
#define DARTS_H

#include <stdint.h>

#define MAX_SCORE 10
#define MIDDLE_SCORE 5
#define LOW_SCORE 1
#define NO_SCORE 0

#define RADIUS_MAX_SCORE 1.0
#define RADIUS_MIDDLE_SCORE 5.0
#define RADIUS_LOW_SCORE 10.0

typedef struct {
    float x;
    float y;
} coordinate_t;


uint8_t score(coordinate_t landing_position);
float radius(coordinate_t landing_position);
#endif
