#! /usr/bin/env python

# http://codeforces.com/problemset/problem/818/F
# Problem name ::: F. Level Generation
# submission number

def max_conn_comp(nodes, edges):
    for i in range(1, nodes+1):
        if i*(i-1)/2 >= edges:
            return nodes - i + 1

def new_binary_search(nodes):
    from math import ceil
    min_edges = 0
    max_edges = int(nodes)
    edges = abs(max_edges-min_edges)//2
    count = 0
    print(edges)
    while True:
        bridges = max_conn_comp(nodes, edges) + 1
        print(bridges, edges)
        if bridges < edges:
            max_edges = edges
            edges = abs(max_edges-min_edges)//2
        elif bridges > edges:
            min_edges = edges
            edges = abs(max_edges-min_edges)//2
        else:
            print("found")
            max_edges = bridges + edges
            return max_edges
        count += 1
        if count > max_edges:
            print("not found")
            break

def binary_search(nodes):
    from math import ceil
    if nodes <= 5:
        return nodes - 1
    if nodes == 7:
        return nodes
    min_edges = 0
    # maximum of "non-bridge" edges cannot excede nodes
    max_edges = nodes
    edges = ceil(abs((max_edges-min_edges))/2)
    print(edges)
    count = 0
    while True:
        # print(nodes, edges)
        ccs = max_conn_comp(nodes, edges)
        bridges = ccs - 1
        if bridges < edges:
            print(bridges, edges)
            max_edges = edges
            edges = ceil(edges/2)
        elif bridges > edges:
            print(bridges, edges)
            min_edges = edges
            edges = ceil((max_edges+edges)/2)
        else:
            max_edges = bridges + edges
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
        # print(binary_search(val))
        print(new_binary_search(val))





if __name__ == '__main__':
    main()
