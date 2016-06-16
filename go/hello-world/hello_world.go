package hello

const testVersion = 2

// HelloWorld says hello
func HelloWorld(string string) string {
	helloString := "Hello, "
	if string != "" {
		helloString += string
	} else {
		helloString += "World"
	}
	return helloString + "!"
}
