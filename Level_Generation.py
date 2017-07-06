#! /usr/bin/env python

# http://codeforces.com/problemset/problem/818/F
# Problem name ::: F. Level Generation
# submission number

def max_conn_comp(nodes, edges):
    for i in range(1, nodes+1):
        if i*(i-1)/2 >= edges:
            return nodes - i + 1


def binary_search(nodes):
    from math import ceil
    min_edges = 0
    # maximum of "non-bridge" edges cannot excede nodes
    max_edges = nodes
    search_term = ceil((max_edges+min_edges)/2)
    count = 0
    while True:
        # print(nodes, search_term)
        ccs = max_conn_comp(nodes, search_term)
        bridges = ccs - 1
        if bridges < search_term:
            # print(bridges, search_term)
            max_edges = search_term
            search_term = ceil(search_term/2)
        elif bridges > search_term:
            # print(bridges, search_term)
            min_edges = search_term
            search_term = ceil((max_edges+search_term)/2)
        else:
            max_edges = bridges + search_term
            # print("max_edges_found = %s" % max_edges)
            # print("max_bridges_found = %s" % bridges)
            return max_edges
        count += 1
        if count > max_edges:
            print("not found")
            break




def main():

    import sys

    data = [line.rstrip() for line in sys.stdin.readlines()]
    num_graphs = data[0]
    graph_sizes = [int(x) for x in data[1:]]

    for val in graph_sizes:
        # print(binary_search(val))
        print(binary_search(val))





if __name__ == '__main__':
    main()
