package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main(){
	var xd []int
	var count int

	data, _ := os.Open("./Day 1/Data.txt")
	defer data.Close()
	scanner := bufio.NewScanner(data)
	for scanner.Scan() {
		heh, _ := strconv.Atoi(scanner.Text())
		xd = append(xd, heh)
	}
	for i, i2 := range xd {
		if i == 0{
			continue
		}
		if i2 > xd[i-1] {
			count++
		}
	}

	fmt.Println(strconv.Itoa(count))

}
