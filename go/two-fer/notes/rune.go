package main

import "fmt"

func main() {
	s1 := "aüa"
	s2 := "aaa"

	var test1 bool = true
	var test2 bool = true

	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			test1 = false
			break
		}
	}

	s1r, s2r := []rune(s1), []rune(s2)

	for i := 0; i < len(s1r); i++ {
		if s1r[i] != s2r[i] {
			test2 = false
			break
		}
	}

	switch test1 {
	case true:
		fmt.Println("s1 and s2 are the same")
	default:
		fmt.Println("s1 and s2 are not the same")
	}

	switch test2 {
	case true:
		fmt.Println("s1r and s2r are the same")
	default:
		fmt.Println("s1r and s2r are not the same")
	}
}
