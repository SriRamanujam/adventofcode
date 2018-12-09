#!/usr/bin/env python3

if __name__ == '__main__':
    things = [int(x) for x in open('input.txt', 'r').read().strip().split()]

    def process(things):
        num_children = things.pop(0)
        num_md_entries = things.pop(0)
        counter = 0

        if num_children == 0:
            for _ in range(num_md_entries):
                counter += things.pop(0)
        else:
            child_sums = []
            for _ in range(num_children):
                child_sums.append(process(things))

            for _ in range(num_md_entries):
                try:
                    counter += child_sums[things.pop(0)-1]
                except IndexError:
                    pass

        return counter

    print("Value of root node: {}".format(process(things)))
