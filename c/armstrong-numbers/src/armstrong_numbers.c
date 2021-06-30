#include "armstrong_numbers.h"

bool is_armstrong_number(int candidate) {
	
	// Check whether the candidate is less than zero
	if (candidate < 0)
		return false;

	int number_of_digits = 0;

	// Get the number of digits in candidate
	for (int tmp_candidate = candidate; tmp_candidate !=0;) {
		tmp_candidate /= 10;
		number_of_digits++;
	}

	int armstrong_result = 0;

	// Loop through all digits and raise them with the number of digits
	for(int tmp_candidate = candidate, digit; tmp_candidate != 0;) {
		digit = tmp_candidate % 10;
		armstrong_result += pow(digit, number_of_digits);
		tmp_candidate /= 10;
	}

	// Return whether the armstrong_result equals candidate
	return (armstrong_result == candidate);
}
	

	
