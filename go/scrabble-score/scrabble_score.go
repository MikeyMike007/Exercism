// Package scrabble provides functionality to convert words into points
// according to the game rules of Scrabble
package scrabble

import (
	"unicode"
)

// Using an array instead of map which seems more eficicent
var pointConverter = []int{
	'a': 1,
	'e': 1,
	'i': 1,
	'o': 1,
	'u': 1,
	'l': 1,
	'n': 1,
	'r': 1,
	's': 1,
	't': 1,
	'd': 2,
	'g': 2,
	'b': 3,
	'c': 3,
	'm': 3,
	'p': 3,
	'f': 4,
	'h': 4,
	'v': 4,
	'w': 4,
	'y': 4,
	'k': 5,
	'j': 8,
	'x': 8,
	'q': 10,
	'z': 10,
	' ': 0,
}

// Score returns the total points of a certain word according to game rules
func Score(word string) int {
	var score int

	// When looping through a string, the w becomes a rune
	for _, w := range word {
		// unicode.toLower takes a rune and outputs a rune
		w := unicode.ToLower(w)
		score += pointConverter[w]
	}
	return score
}
