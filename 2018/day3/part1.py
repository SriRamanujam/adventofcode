#!/usr/bin/env python3

import numpy as np
from scipy import ndimage

# indexing rules:
# fabric[y:y+len, x:x+len] += 1 to mark dirty
# fabri[y:y+len, x:x+len] to access
# array is a representation of each square inch of fabric
fabric = np.zeros((1000, 1000), dtype=int) # all zeros to start

for line in open('input.txt', 'r').readlines():
    coords, dims = line.split('@ ')[1].split(': ')
    x, y = map(int, coords.split(','))
    w, h = map(int, dims.split('x'))

    fabric[y:y+h, x:x+w] += 1 #increment dirty regions

# now all we have to do is count the number of square inches claimed by more than one elf
print("Total surface area claimed by two or more elves: {}".format(np.count_nonzero(fabric > 1)))

# uncomment this if you want to see the matrix plotted out
#import matplotlib.pyplot as plt
#np.set_printoptions(threshold=np.inf, linewidth=1000)
#plt.matshow(fabric)
#plt.show()
