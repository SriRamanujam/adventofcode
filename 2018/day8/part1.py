#!/usr/bin/env python3

if __name__ == '__main__':
    things = [int(x) for x in open('input.txt', 'r').read().strip().split()]

    metadata_sum = 0

    def process(things, md_sum=0):
        num_children = things.pop(0)
        num_md_entries = things.pop(0)
        counter = 0

        for _ in range(num_children):
            counter += process(things, md_sum)

        for _ in range(num_md_entries):
            counter += things.pop(0)

        return md_sum + counter

    print("Sum: {}".format(process(things)))
