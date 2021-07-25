#include "leap.h"

namespace leap {
    bool is_leap_year(int year) {
        // Return true if year is evenly divisible by 4, and,
        // year is evenly divisible with 400 and not evenly divisible with 100.
        if ((year % 4 == 0) && ((year % 400 == 0) || (year % 100 != 0)))
                return true;

        return false;
    }
}  // namespace leap
