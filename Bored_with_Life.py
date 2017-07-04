#! /usr/bin/env python

# http://codeforces.com/problemset/problem/822/A
# Problem name ::: A. I'm bored with life
# submission number 28275402 (Accepted)

# given positive numbers n,m: GCD(n!, m!) must be
# simply min(n,m)! because the factorial of the smaller
# number must be the largest divisor of the factorial
# of both numbers

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
