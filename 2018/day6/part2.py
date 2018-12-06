#!/usr/bin/env python3

from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    coords = []

    for line in [x.strip() for x in open('input.txt', 'r').readlines()]:
        x, y = line.split(', ')
        coords.append([int(x), int(y)])

    xvalues = np.array([x[0] for x in coords])
    yvalues = np.array([x[1] for x in coords])

    grid = np.zeros((max(xvalues)+1, max(yvalues)+1), dtype=int)

    with np.nditer(grid, flags=['multi_index'], op_flags=['readwrite']) as it:
        while not it.finished:
            manhattans = 0
            for coord in coords:
                manhattans += distance.cityblock(coord, list(it.multi_index))
            grid[it.multi_index[0], it.multi_index[1]] = manhattans
            it.iternext()

    answer = np.count_nonzero(grid < 10000)
    print("The size of the region with has a total distance less than 10000 is {}".format(answer))

    # uncomment if you want to see a visualization of the totals
    #plt.matshow(grid)
    #plt.show()
