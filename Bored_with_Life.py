#! /usr/bin/env python

# http://codeforces.com/problemset/problem/822/A
# Problem name ::: A. I'm bored with life
# submission number 


def factorial(n):
    value = 1
    if n <= value:
        return value
    
    for x in range(2, n + 1):
        value *= x

    return value


def main():

    import sys

    for line in sys.stdin:
        line = [int(x) for x in line.rstrip().split(" ")]
        a = line[0]
        b = line[1]
        print(factorial(min(line)))


if __name__ == '__main__':
    main()
