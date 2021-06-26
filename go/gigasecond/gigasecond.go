// Package gigasecond provides functionality to add 1e9 seconds to a time.
package gigasecond

import "time"

const Gigasecond = time.Second * 1e9

// AddGigasecond returns time after 1e9 seconds from a specific time
func AddGigasecond(t time.Time) time.Time {
	return t.Add(Gigasecond)
}
