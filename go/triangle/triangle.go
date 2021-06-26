// Package triangle provides functionality of categorising triangles
package triangle

import (
	"sort"
	"math"
)

// Kind indicates the type of triangle e.g. Equilateral, Isosceles, Scalene
type Kind int

const (
	  // NaT = Not a Triangle
		NaT Kind = iota
		// Equ = Equilateral
		Equ           
		// Iso = Isosceles
		Iso            
		// Sca = Scalene
		Sca          
)

// KindFromSides returns a categorisation of a triangle with sides a, b and c
func KindFromSides(a, b, c float64) Kind {
	var k Kind
	maxSides := 0
	allSides := [3]float64{a, b, c}
	sort.Float64s(allSides[:])

	for _, value := range allSides {
		if value <= 0 || math.IsNaN(value) || math.IsInf(value,0) {
			return NaT
		}
	}

	if allSides[0] + allSides[1] < allSides[2] {
		return NaT
	}

	mapAllSides := make(map[float64]int)
	mapAllSides[a]++
	mapAllSides[b]++
	mapAllSides[c]++

	for _, value := range mapAllSides {
		if value > maxSides {
			maxSides = value
		}
	}

	switch maxSides {
	case 3:
		k = Equ
	case 2:
		k = Iso
	case 1:
		k = Sca
	default:
		k = NaT
	}
	
	return k
}
