#!/usr/bin/python3
from collections import Counter

twos = set()
threes = set()

for line in open('input.txt', 'r').readlines():
    counts = Counter(line.strip())
    for letter in counts:
        if counts[letter] == 2 and line not in twos:
            twos.add(line)
        if counts[letter] == 3 and line not in threes:
            threes.add(line)

twos = len(twos)
threes = len(threes)
print("Number of twos: {}\tNumber of threes: {}".format(twos, threes))
print("Checksum: {}".format(twos * threes))
