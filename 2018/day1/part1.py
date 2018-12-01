#!/usr/bin/python3

if __name__ == '__main__':
    print(sum(map(lambda x: int(x), open('input.txt', 'r').readlines())))
