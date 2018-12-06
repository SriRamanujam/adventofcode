#!/usr/bin/env python3

from scipy.spatial import distance
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    coords = []

    for line in [x.strip() for x in open('input.txt', 'r').readlines()]:
        x, y = line.split(', ')
        coords.append([int(x), int(y)])

    xvalues = np.array([x[0] for x in coords])
    yvalues = np.array([x[1] for x in coords])

    # notes after looking at the visualization:
    # the general algorithm will be to create a grid that is slightly bigger on
    # either side than the max, then for every marker go through and mark every
    # point with the closest. if a point ends up being closer to one after it
    # has been marked with another, update. if a duplicate happens, mark it as a dup
    # with its value.
    # after you have done that for every point in the input, look at each EDGE point.
    # any markers that edge points think are closest are by nature unbounded and can
    # be eliminated from contention. get the nonzero counts of whatever's left and there you go.

    grid = np.zeros((max(xvalues)+1, max(yvalues)+1), dtype=int)
    manhattans = np.empty((max(xvalues)+1, max(yvalues)+1), dtype=int)
    manhattans.fill(9999)

    for idx, coord in enumerate(coords):
        print("Updating for coordinate idx {}, {}".format(idx + 1, coord))
        it = np.nditer(grid, flags=['multi_index'], op_flags=['writeonly'])
        while not it.finished:
            manhattan = distance.cityblock(coord, list(it.multi_index))
            x = it.multi_index[0]
            y = it.multi_index[1]
            if manhattan == manhattans[x, y]:
                it[0] = -1 # to denote a tie so it shouldn't count for anything
            elif manhattan < manhattans[x, y]:
                manhattans[x, y] = manhattan
                it[0] = idx

            it.iternext()

    skiplist = set()
    it2 = np.nditer(np.concatenate([grid[0,:-1], grid[:-1,-1], grid[-1,::-1], grid[-2:0:-1,0]]))
    while not it2.finished:
        skiplist.add(np.asscalar(it2[0]))
        it2.iternext()

    final_answer = {}
    for idx, coord in enumerate(coords):
        if idx not in skiplist:
            final_answer[idx] = np.count_nonzero(grid == idx)

    max_key = max(final_answer.keys(), key=(lambda key: final_answer[key]))
    print("The most bounded area is coordinate {}, with area {}".format(coords[max_key], final_answer[max_key]))

    # uncomment if you want to see the plot of the coordinates
    #plt.plot(xvalues, yvalues, marker='.', color='k', linestyle='none')
    #plt.show()

    # uncomment if you want to see the final regions
    #plt.matshow(grid)
    #plt.show()
