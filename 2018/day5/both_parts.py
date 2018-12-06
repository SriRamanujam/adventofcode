#!/usr/bin/env python3

def collapse_polymer(poly_str):
    poly_chars_list = list(poly_str)
    new_polymer_stack = []
    while True:
        try:
            char1 = poly_chars_list.pop()
        except IndexError:
            return new_polymer_stack[::-1]
        try:
            char2 = poly_chars_list.pop()
        except IndexError:
            new_polymer_stack.append(char1)
            return new_polymer_stack[::-1]

        if char1 == char2.swapcase():
            continue
        else:
            new_polymer_stack.append(char1)
            poly_chars_list.append(char2)



if __name__ == '__main__':
    polymer = open('input.txt', 'r').read().strip()

    def perform_polymer_collapse(polymer_iteration):
        while True:
            temp = polymer_iteration
            polymer_iteration = collapse_polymer(polymer_iteration)

            # if the collapse cannot find anything more to collapse, the two
            # strings should be the same and we can break out and return
            if polymer_iteration == temp:
                break
        return polymer_iteration

    polymer_iteration = perform_polymer_collapse(polymer)
    print("Part1 answer: final length is {}".format(len(polymer_iteration)))

    def do_part_2(polypoly, char):
        print("Computing result with letter {}".format(char))
        charlist = [char.lower(), char.upper()]

        return len(perform_polymer_collapse(''.join(c for c in polypoly if c not in charlist)))

    results = {}
    for i in list('abcdefghijklmnopqrstuvwxyz'):
        results[i] = do_part_2(''.join(polymer_iteration), i)

    min_letter = 50000
    what_letter = ''
    for k, v in results.items():
        if v < min_letter:
            min_letter = v
            what_letter = k

    print("Part 2: max letter is {} with {}".format(what_letter, min_letter))
