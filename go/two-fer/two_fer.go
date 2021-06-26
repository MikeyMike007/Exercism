// Package twofer contains the function ShareWith
package twofer

// Function ShareWith returns a string that describes how you should Share
// something between someone and yourself
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}

	return "One for " + name + ", one for me."
}
