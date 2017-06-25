#! /usr/bin/env python

# http://codeforces.com/problemset/problem/765/C
# Problem name ::: C. Table Tennis Game 2
# submission number 28020392 (Accepted)


def compute_next_palidrome(time_input):
    


def compute_sets(a, b, k):
    if not(a >= k or b >= k):
        return -1

    awins = a // k
    bwins = b // k

    if awins == 0:
        if b % k != 0:
            return -1

    elif bwins == 0:
        if a % k != 0:
            return -1

    return awins + bwins


def main():

    import sys

    for line in sys.stdin:
        line = [int(x) for x in line.rstrip().split(" ")]
        k = line[0]
        a = line[1]
        b = line[2]
        print(compute_sets(a,b,k))


if __name__ == '__main__':
    main()