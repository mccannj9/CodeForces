#! /usr/bin/env python

# http://codeforces.com/problemset/problem/818/F
# Problem name ::: F. Level Generation
# submission number 29524117 (Accepted)


def level_generation(n):
    from math import floor, ceil, sqrt

    # n total nodes where one component has x nodes
    # the rest of the components have only 1 node each
    # max edges in x component = (x choose 2) = x^2 - x
    # we need x^2-x <= 2(n - x) per the problem statement
    # where n - x is the number of bridges
    # x^2 + x <= 2n
    # (x + 1/2)^2-1/4 <= 2n
    # x <= sqrt(2n+1/4)-1/2
    z = 2*n+1/4
    quad_solv = sqrt(2*n+1/4)-1/2
    print(z)
    print(quad_solv)
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
