#!/usr/bin/env python3
import itertools

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def check_equal(list1, list2):
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True


def do_the_thing(poly_str):
    poly_copy = poly_str

    thing = list(poly_str)
    temp = []
    while True:
        try:
            char1 = thing.pop()
        except IndexError:
            return temp[::-1]
        try:
            char2 = thing.pop()
        except IndexError:
            temp.append(char1)
            return temp[::-1]

        if char1 == char2.swapcase():
            continue
        else:
            temp.append(char1)
            thing.append(char2)



if __name__ == '__main__':
    polymer = open('input.txt', 'r').read().strip()

    def oh_jeez(what_this_do):
        while True:
            what_this_do_old = what_this_do
            what_this_do = do_the_thing(what_this_do)

            if what_this_do == what_this_do_old:
                break
        return what_this_do

    what_this_do = oh_jeez(polymer)
    print("Part1 answer: final length is {}".format(len(what_this_do)))

    def do_part_2(polypoly, char):
        print("Computing result with letter {}".format(char))
        charlist = [char.lower(), char.upper()]

        return len(oh_jeez(''.join(c for c in polypoly if c not in charlist)))

    results = {}
    for i in list('abcdefghijklmnopqrstuvwxyz'):
        results[i] = do_part_2(''.join(what_this_do), i)

    min_letter = 50000
    what_letter = ''
    for k, v in results.items():
        if v < min_letter:
            min_letter = v
            what_letter = k

    print("Part 2: max letter is {} with {}".format(what_letter, min_letter))
