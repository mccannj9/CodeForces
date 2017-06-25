#! /usr/bin/env python

# http://codeforces.com/problemset/problem/817/A
# Problem name ::: A. Treasure Hunt
# Submission Number: 28041271 (Accepted)

# Key Ideas:

# m and n are numbers to check if going between the x and
# y positions is even possible regardless of constraint
# that you must move them together

# next, the difference between m and n has to be even,
# otherwise you can't go to the treasure

def main():

    import sys

    data = [line.rstrip().split() for line in sys.stdin.readlines()]
    positions = [int(x) for x in data[0]]
    moves = [int(x) for x in data[1]]

    x1, y1 = positions[0], positions[1]
    x2, y2 = positions[2], positions[3]

    x, y = moves[0], moves[1]

    m = (x2 - x1) / x
    n = (y2 - y1) / y

    if m.is_integer() and n.is_integer() and (int(m) - int(n)) % 2 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
