#!/usr/bin/env python3

if __name__ == '__main__':
    seen = set()
    current = 0
    num_iters = 0
    frequencies = [int(x) for x in open('input.txt', 'r').readlines()]

    while True:
        num_iters += 1
        for freq in frequencies:
            current += freq
            if current in seen:
                print("The answer is {}".format(current))
                exit(0)
            else:
                seen.add(current)
