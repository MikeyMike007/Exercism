
package main

import "fmt"

// Proverb 
func Proverb(rhyme []string) []string {
	proverb := make([]string, len(rhyme))

	for i := 0; i < len(rhyme) - 1; i++ {
		proverb[i] = fmt.Sprintf("For want of a %s the %s was lost.", rhyme[i], rhyme[i+1])
	}
	proverb[len(rhyme) - 1] = fmt.Sprintf("And all for the want of a %s.", rhyme[0])

	return proverb
}

func main() {
	var test []string
	test1 := []string{
		"foot",
		"nail",
		"street",
		"test",
	}
	test = Proverb(test1)
	fmt.Println(test)
	fmt.Println(test[0])
}
