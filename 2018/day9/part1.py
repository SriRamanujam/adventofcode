#!/usr/bin/env python3
from collections import deque

if __name__ == '__main__':
    parts = open('input.txt', 'r').read().split()

    num_players = int(parts[0])
    last_marble = int(parts[6])

    circle = deque([0])
    scores = [0] * num_players

    for i in range(1, last_marble+1):
        cur_player = (i-1) % num_players
        #print("Current player: {}".format(cur_player), end=': ')
        #print("Marble: {}".format(i), end=',')
        if i % 23 == 0:
            circle.rotate(7)
            scores[cur_player] += (i + circle.pop())
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)

        # circle printing logic
        #print('[', end='')
        #for idx, marble in enumerate(circle):
        #    if idx == cur_pos:
        #        print(', ({})'.format(marble), end='')
        #    else:
        #        print(', {}'.format(marble), end='')
        #print(']')

    print('Max score: {}'.format(max(scores)))
