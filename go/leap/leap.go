// Package leap provides functionality on assessing whther a certain year is a
// leap year 
package leap

// IsLeapYear assesses whther a certain year is a leap year
func IsLeapYear(year int) bool {
	if year % 4 == 0 {
		if year % 100 == 0 && year % 400 == 0 {
			return true
		} else if year % 100 == 0 {
			return false
		} else {
			return true
		}
	}
	return false
}
