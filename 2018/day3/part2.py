#!/usr/bin/env python3

import numpy as np

def get_claim(area):
    return fabric[area['y']:area['y']+area['h'], area['x']:area['x']+area['w']]

fabric = np.zeros((1000,1000), dtype=int)
areas = []

for line in open('input.txt', 'r').readlines():
    coords, dims = line.split('@ ')[1].split(': ')
    x, y = map(int, coords.split(','))
    w, h = map(int, dims.split('x'))

    areas.append({'x': x, 'y': y, 'w': w, 'h': h})
    fabric[y:y+h, x:x+w] += 1 #increment dirty regions

for idx, area in enumerate(areas):
    claim = get_claim(area)
    if np.count_nonzero(claim > 1) == 0:
        print("Claim entirely owned by a single elf: {}".format(idx + 1))

# uncomment this if you want to see the matrix plotted out
#import matplotlib.pyplot as plt
#plt.matshow(fabric, cmap=plt.get_cmap("viridis"))
#plt.show()
