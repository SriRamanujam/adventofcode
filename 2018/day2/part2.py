#!/usr/bin/python3

## nb: it is expected that you have run pipenv install prior to running this script!

import numpy as np
from Levenshtein import distance

raw_lines = [line.strip() for line in open('input.txt', 'r').readlines()]
lines = np.array(raw_lines)

# use levenshtein array as a predicate function to calculate distances between
# all pairs of strings in the list
vdistance = np.vectorize(distance)
lev_array = vdistance(lines, lines[:, np.newaxis])

# get indices of all occurrences of 1 levenshtein distance (only one different letter)
# there should be only one pair, represented twice in the final output
off_by_one = (lev_array == 1).nonzero()
if (len(off_by_one) != 2):
    print("Something has gone wrong, there is more than one valid pair!")
    print(off_by_one)
else:
    print("Your two differing strings:")
    print(raw_lines[off_by_one[0][0]] + " and " + raw_lines[off_by_one[0][1]])

    print("Difference between the two (final answer): ", end='')
    combined = zip(raw_lines[off_by_one[0][0]], raw_lines[off_by_one[0][1]])
    for i,j in combined:
        if i == j:
            print(i, end='')
    print()
