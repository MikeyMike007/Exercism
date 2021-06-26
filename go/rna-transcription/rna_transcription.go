// Package strand provides functionality to return the RNA complement of a DNA
// strand

package strand

// ToRNA returns the complement of a DNA strand
func ToRNA(dna string) string {

	var complementDNA string
	complement := map[string]string{
		"G": "C",
		"C": "G",
		"T": "A",
		"A": "U",
	}

	for _, char := range dna {
		complementDNA += complement[string(char)]
	}

	return complementDNA
}
