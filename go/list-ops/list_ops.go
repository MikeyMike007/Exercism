// Package listops provides functionality of traditional list operations without
// using existing pre-built functions in golang
package listops

// As defined in the list_ops_test.go
type binFunc func(x, y int) int
type predFunc func(x int) bool
type unaryFunc func(x int) int

// IntList is a list of integers
type IntList []int

// Length (given a list, return the total number of items within it)
func (list IntList) Length() int {
	var length int

	for range list {
		length++
	}

	return length
}

// Reverse (given a list, return a list with all the original items, but in reversed order)
func (list IntList) Reverse() IntList {

	// Check if list is empty
	if list.Length() == 0 {
		return list
	}

	var reversedList IntList
	var currentLength int

	// Make a copy so you dont change the list
	tmpList := make(IntList, list.Length())
	copy(tmpList, list)
	for range tmpList {
		currentLength = tmpList.Length()
		reversedList = append(reversedList, tmpList[currentLength-1])
		// Cut off a piece in the end for every loop
		tmpList = tmpList[:currentLength-1]
	}
	return reversedList
}

// Append adds all items in the input list to the end of current list
func (list IntList) Append(otherList IntList) IntList {

	if list.Length() == 0 {
		return otherList
	} else if otherList.Length() == 0 {
		return list
	}

	appendedList := make(IntList, list.Length()+otherList.Length())
	copy(appendedList, list)
	// Add to the end of the appendedList
	copy(appendedList[list.Length():], otherList)
	return appendedList
}

// Foldl (given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left using function(accumulator, item))
func (list IntList) Foldl(function binFunc, intialAccumulator int) int {
	accumulator := intialAccumulator

	for _, value := range list {
		accumulator = function(accumulator, value)
	}
	return accumulator
}

// Foldr (given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right using function(item, accumulator))
func (list IntList) Foldr(function binFunc, initialAccumulator int) int {
	accumulator := initialAccumulator
	var currentLength int
	tmpList := make(IntList, list.Length())
	copy(tmpList, list)

	for range tmpList {
		currentLength = tmpList.Length()
		accumulator = function(tmpList[currentLength-1], accumulator)
		tmpList = tmpList[:currentLength-1]
	}
	return accumulator
}

// Map (given a function and a list, return the list of the results of applying function(item) on all items)
func (list IntList) Map(function unaryFunc) IntList {
	mappedList := make(IntList, list.Length())
	for index, value := range list {
		mappedList[index] = function(value)
	}
	return mappedList
}

// Filter (given a predicate and a list, returns the list of all items for which predicate(item) is True)
func (list IntList) Filter(function predFunc) IntList {

	if list.Length() == 0 {
		return list
	}

	var filterList IntList

	for _, value := range list {
		if function(value) {
			// Need to put the value in a temporary list in order to be able to
			// use the Append function
			tmpList := IntList{value}
			filterList = filterList.Append(tmpList)
		}
	}
	return filterList
}

// Concat combines all items in all lists into one flattened list
func (list IntList) Concat(listofLists []IntList) IntList {
	for _, l := range listofLists {
		list = list.Append(l)
	}
	return list
}
