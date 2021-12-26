package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("./input")
	if err != nil {
		log.Fatal("life is hard, couldn't open file")
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	increases := 0
	prev := -1
	values := []int{}
	for scanner.Scan() {
		if i, err := strconv.Atoi(scanner.Text()); err == nil {
			if prev != -1 && i > prev {
				increases += 1
			}
			prev = i
			values = append(values, i)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal("sad times, something went wrong scanning the file")
		os.Exit(1)
	}

	fmt.Println("Part 1: Number of increases: ", increases)

	window_sum := values[0] + values[1] + values[2]
	increases = 0
	for i := 3; i < len(values); i++ {
		new_sum := window_sum + values[i] - values[i-3]

		if new_sum > window_sum {
			increases++
		}
		window_sum = new_sum
	}

	fmt.Println("Part 2: Number of increases: ", increases)
}
