// Package hamming provides functionality on calculate the Hamming difference
// between two DNA strands
package hamming

import "errors"

// Distance calculates tthe Hemming difference between two DNA strands
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, errors.New("strings have different lengths")
	}

	var count int

	for i := 0; i <= len(a)-1; i++ {
		if a[i] != b[i] {
			count++
		}
	}
	return count, nil
}
