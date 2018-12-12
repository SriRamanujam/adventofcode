#!/usr/bin/env python3

import re
import copy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    lines = [x.strip() for x in open('input.txt', 'r').readlines()]

    regex = re.compile("position=<(?P<position>[\s\d-]+, [\s\d-]+)> velocity=<(?P<velocity>[\s\d-]+, [\s\d-]+)>")

    positions = []
    velocities = []
    for line in lines:
        matches = regex.findall(line)
        x, y = map(int, matches[0][0].split(', '))
        dx, dy = map(int, matches[0][1].split(', '))
        positions.append([x, y])
        velocities.append([dx, dy])

    # So, ostensibly this solution involves training a computer to recognize
    # that a configuration of points on the graph spelled out letters. This
    # would normally take some sort of deep-learning algo and a Ph.D to
    # accomplish.
    # Tom instead had the idea to see if the answer would be the "frame", as it
    # were, where the bounding box of all the points was the smallest. So we're
    # going to try that first.

    def bounding_box(points):
        x_coords, y_coords = zip(*points)
        l = max(x_coords) - min(x_coords)
        w = max(y_coords) - min(y_coords)
        return l * w

    #plt.scatter(*zip(*positions))
    #plt.show()

    smallest_box = bounding_box(positions)
    print("Starting area: {}".format(smallest_box))
    smallest_list = []
    num_iters = 0
    while True:
        #print("Iteration {}".format(num_iters))
        bounds = bounding_box(positions)
        if bounds <= smallest_box:
            num_iters += 1
            list_copy = copy.deepcopy(positions)
            #print("New smallest box: {}".format(bounds))
            smallest_box = bounds
            # update positions using velocity vector
            for idx in range(len(positions)):
                x, y = positions[idx]
                dx, dy = velocities[idx]
                positions[idx] = ( x + dx, y + dy )
        else:
            # bounding box is getting bigger, so break out and return the last
            # iteration's (which would be the smallest) position vectors
            print("Smallest area: {}".format(bounding_box(list_copy)))
            print("Number of seconds taken: {}".format(num_iters-1))
            print("Note that picture is inverted. Save a copy and flip it around to see the answer!")
            plt.scatter(*zip(*list_copy))
            plt.show()
            break
