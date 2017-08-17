#! /usr/bin/env python

# http://codeforces.com/problemset/problem/818/F
# Problem name ::: F. Level Generation
# submission number 29524117 (Accepted)


def level_generation(n):
    from math import floor, ceil, sqrt

    quad_solv = sqrt(2*n+1/4)-1/2
    x = floor(quad_solv)
    y = ceil(quad_solv)

    xed = int(x*(x-1)/2 + n - x)
    xbr = n - x

    ybr = n - y
    yed = 2*ybr

    if xed > yed:
        print(xed)
    else:
        print(yed)

    return


def main():

    import sys

    data = [line.rstrip() for line in sys.stdin.readlines()]
    num_graphs = data[0]
    graph_sizes = [int(x) for x in data[1:]]

    for val in graph_sizes:
        level_generation(val)


if __name__ == '__main__':
    main()
