#!/usr/bin/env python3

if __name__ == '__main__':
    seen = []
    current = 0
    num_iters = 0
    frequencies = list(map(lambda x: int(x), open('input.txt', 'r').readlines()))

    while True:
        num_iters += 1
        print("Iteration {}".format(num_iters))
        for freq in frequencies:
            current += freq
            if current in seen:
                print(current)
                exit(0)
            else:
                seen.append(current)

