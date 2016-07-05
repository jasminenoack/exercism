// Clock stub file

// Package clock handles the clock
package clock

import "fmt"

const testVersion = 4

// Clock API as stub definitions.  No, it doesn't compile yet.
// More details and hints are in clock_test.go.

// Clock date independent clock
type Clock struct {
	totalMinutes int
}

// New create a new clock
func New(hour, minute int) Clock {
	return Clock{totalMinutes: simplifyTime(hour*60 + minute)}
}

// String returns the time as a string
func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.totalMinutes/60, c.totalMinutes%60)
}

// Add adds minutes to the clock
func (c Clock) Add(minutes int) Clock {
	c.totalMinutes = simplifyTime(c.totalMinutes + minutes)
	return c
}

func simplifyTime(minutes int) int {
	minutesInDay := 24 * 60
	return ((minutes % minutesInDay) + minutesInDay) % minutesInDay
}
