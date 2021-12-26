package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func main() {
	part1()
	part2()
}

func part1() {
	file, err := os.Open("./input")
	if err != nil {
		log.Fatal("life is hard, couldn't open file")
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	// nb: gamma and epsilon are inverses
	// there are a thousand entries in the input
	// 12 bits per entry
	// we are going to cheat a bit here by hardcoding some assumptions
	// they have to have it set up such that no one column of bits is exactly split 500-500
	// therefore we just need to count up how many 1 bits are in each column
	// if > 500: epsilon is 1, if < 500, epsilon is 0 for that bit
	// only 12 bits per line, so array can be hardcoded to 12
	// once we have epsilon, invert it to find gamma and multiply

	bits := [12]int{}

	for scanner.Scan() {
		for idx, bit := range scanner.Text() {
			if bit == '1' {
				bits[idx]++
			}
		}
	}

	epsilonStr := ""
	for _, bit := range bits {
		if bit >= 500 {
			epsilonStr += "1"
		} else {
			epsilonStr += "0"
		}
	}

	epsilon, err := strconv.ParseInt(epsilonStr, 2, 64)

	if err != nil {
		log.Fatalf("truly, we are lost, could not convert %s to a valid number", epsilonStr)
		os.Exit(1)
	}

	log.Printf("value of epsilon: %s => %d", epsilonStr, epsilon)

	// convert epsilon to gamma by flipping 12 least significant bits and leaving the rest alone
	var t int64 = 1
	gamma := epsilon
	for t <= gamma {
		gamma = gamma ^ t
		t = t << 1
	}

	log.Printf("value of gamma: %d", gamma)

	log.Printf("Part 1: gamma x epsilon = %d", gamma*epsilon)
}

func part2() {

}
