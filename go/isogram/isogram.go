// Package isogram provides functionality to determine whether a word is a
// isogram
package isogram

import "unicode"

// IsIsogram check if a word is an isogram. Returns true if it is, else it
// returns false
func IsIsogram(wordCandidate string) bool {

	// make a map to keep track of all the runes in the wordCandidate and their
	// occurence
	candidateMap := make(map[rune]int)

	for _, character := range wordCandidate {
		// using the unicode library to check wether the rune is a character
		if unicode.IsLetter(character) {
			// save a lower case rune to the map
			candidateMap[unicode.ToLower(character)]++
		}
	}

	for _, runeOccurence := range candidateMap {
		// return false if a occurence for a certain rune is larger than one
		if runeOccurence > 1 {
			return false
		}
	}
	return true
}
