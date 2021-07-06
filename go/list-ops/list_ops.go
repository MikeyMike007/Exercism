package main

import "fmt"

type intList []int

// Length calculates the length of a list
func main() {
	test := intList{
		1,
		2,
		3,
	}

	count := test.Length()
	fmt.Println(count)

}

func (list intList) Length() int {
	var length int

	// Could also have done for range list { length++ }
	for range list {
		length++
	}

	return length
}
