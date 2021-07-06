// Package raindrops provides functionality to convert a number to a raindrop
// sound
package raindrops

import "strconv"

// Convert converts a number to its sound
func Convert(number int) string {

	var raindropSound string

	var numberToSoundConverter = []struct {
		soundNumber int
		sound       string
	}{
		{3, "Pling"},
		{5, "Plang"},
		{7, "Plong"},
	}

	for _, conversionElement := range numberToSoundConverter {
		if number%conversionElement.soundNumber == 0 {
			raindropSound += conversionElement.sound
		}
	}

	if raindropSound != "" {
		return raindropSound
	}

	return strconv.Itoa(number)
}
