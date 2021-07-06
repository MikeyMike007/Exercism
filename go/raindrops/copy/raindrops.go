// Package raindrops provides functionality to convert a number to a raindrop
// sound
package raindrops

import (
	"sort"
	"strconv"
)

// Convert converts a number to its sound
func Convert(number int) string {

	var raindropSound string

	// Slice named keys which will keep the keys of the map numberToSound in order
	var keys []int

	numberToSound := map[int]string{
		3: "Pling",
		5: "Plang",
		7: "Plong",
	}

	// Append the keys in the numberToSound map into a slice named keys
	for k := range numberToSound {
		keys = append(keys, k)
	}

	// Sort the keys
	sort.Ints(keys)

	for _, key := range keys {
		if number%key == 0 {
			raindropSound += numberToSound[key]
		}
	}

	if raindropSound != "" {
		return raindropSound
	}

	return strconv.Itoa(number)
}
