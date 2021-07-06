// Package listops provides functionality of traditional list operations without
// using existing pre-built functions in golang
package listops

// These are defined in list_ops_test.go
type binFunc func(x, y int) int
type predFunc func(x int) bool
type unaryFunc func(x int) int
type intList []int

func (list intList) Filter(function predFunc) intList {
	filterList := make(intList, list.Length())
	lengthFilterList := 0

	for _, value := range list {
		if function(value) {
			filterList[lengthFilterList] = value
			lengthFilterList++
		}
	}
	return filterList[:lengthFilterList]
}

func (list intList) Map(function unaryFunc) intList {
	mapList := make(intList, list.Length())
	for index, value := range list {
		mapList[index] = function(value)
	}

	return mapList
}

func (list intList) Concat(lists []intList) intList {
	for _, listConcat := range lists {
		list.Append(listConcat)
	}
	return list
}

// Length calculates the length of a list
func (list intList) Length() int {
	var length int

	// Could also have done for range list { length++ }
	for index := range list {
		length = index
	}

	return length + 1
}

// Append adds all items in a certain list to the end of the first list
func (list intList) Append(otherList intList) intList {
	appendedList := make(intList, list.Length()+otherList.Length())
	copy(appendedList, list)
	copy(appendedList[list.Length():], otherList)
	return appendedList
}

// Reverse inputs a slice and returns a reversed copy of the input slice
func (list intList) Reverse() intList {
	length := list.Length()
	reversedList := make(intList, length)

	for i := length - 1; i >= 0; i-- {
		reversedList[length-i] = list[i]
	}
	return reversedList
}

// Foldl folds each item in a list with helo of a function and accumulator from the left
func (list intList) Foldl(function binFunc, accumulator int) {
	for _, value := range list {
		accumulator = function(accumulator, value)
	}
}

// Foldl folds each item in a list with helo of a function and accumulator from
// the right
func (list intList) Foldr(function binFunc, accumulator int) {
	for i := list.Length(); i > 0; i-- {
		accumulator = function(accumulator, list[i])
	}
}
