#! /usr/bin/env python

# http://codeforces.com/problemset/problem/822/B
# Problem name ::: B. Crossword Solving
# submission number

def grab_substrings(input):
    return [
        input[i:j + 1] for i in range(len(input)) for j in range(i, len(input))
    ]

def main():

    import sys

    data = [line.rstrip().split() for line in sys.stdin.readlines()]
    lengths = [int(x) for x in data[0]]
    s = data[1][0]
    t = data[2][0]
    print(grab_substrings(s))


if __name__ == '__main__':
    main()
