package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main(){
	var xd []string
	var depth int
	var hPosition int

	data, _ := os.Open("./Day 2/Data.txt")
	defer data.Close()
	scanner := bufio.NewScanner(data)
	for scanner.Scan() {
		heh := scanner.Text()
		xd = append(xd, heh)
	}

	for _, i2 := range xd {
		fuckyou := string(i2[0])
		switch fuckyou {
		case "f":
			wtf, _ := strconv.Atoi(string (i2[len(i2)-1]))
			hPosition += wtf
			break
		case "d":
			wtf, _ := strconv.Atoi(string (i2[len(i2)-1]))
			depth += wtf
			break
		default:
			wtf, _ := strconv.Atoi(string (i2[len(i2)-1]))
			depth -= wtf
			break
		}
	}

	fmt.Println(strconv.Itoa(depth*hPosition))

}
