package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	pos := 0
	depth := 0

	file, err := os.Open("./input")
	if err != nil {
		log.Fatal("life is hard, couldn't open file")
		os.Exit(1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())

		n, err := strconv.Atoi(fields[1])
		if err != nil {
			log.Fatal("life is hard, string parsing did not work")
			os.Exit(1)
		}

		if fields[0] == "forward" {
			pos += n
		} else if fields[0] == "down" {
			depth += n
		} else if fields[0] == "up" {
			depth -= n
		} else {
			log.Fatal("Unknown directive ", fields[0])
			os.Exit(1)
		}
	}

	fmt.Printf("Part 1: depth %d x pos %d = %d\n", depth, pos, depth*pos)

	// reset the file and create a new scanner for part 2
	_, err = file.Seek(0, 0)
	if err != nil {
		log.Fatal("the gods are not with us, could not seek back to start of file")
		os.Exit(1)
	}

	scanner = bufio.NewScanner(file)
	pos = 0
	depth = 0
	aim := 0

	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())

		n, err := strconv.Atoi(fields[1])
		if err != nil {
			log.Fatal("life is hard, string parsing did not work")
			os.Exit(1)
		}

		if fields[0] == "forward" {
			pos += n
			depth += aim * n
		} else if fields[0] == "down" {
			aim += n
		} else if fields[0] == "up" {
			aim -= n
		} else {
			log.Fatal("Unknown directive ", fields[0])
			os.Exit(1)
		}
	}

	fmt.Printf("Part 2: depth %d x pos %d = %d\n", depth, pos, depth*pos)

}
