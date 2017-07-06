#! /usr/bin/env python

# http://codeforces.com/problemset/problem/822/B
# Problem name ::: B. Crossword Solving
# submission number

def max_conn_comp(nodes, edges):
    for i in range(1, nodes+1):
        if i*(i-1)/2 >= edges:
            return nodes - i + 1


# def binary_search(nodes):
#     from math import ceil
#     max_edges = int(nodes*(nodes-1)/2)
#     min_edges = int(nodes-1)
#     min_edges = 0
#     # search_term = (max_edges+min_edges)/2
#     print('_________________________________')
#     print('nodes  |  edges  |  comp  |  bridge ')

#     for search_term in range(min_edges, max_edges + 1):
#         ccs = max_conn_comp(nodes, search_term)
#         print("  %s    |   %s   |   %s   |   %s     |" % (nodes, search_term, ccs, ccs-1))
#     return ccs


def binary_search(nodes):
    from math import ceil
    max_edges = int(nodes*(nodes-1)/2)
    min_edges = 0
    search_term = (max_edges+min_edges)/2
    max_edges_found = 0
    max_bridges_found = 0
    print("searching for nodes = %s" % nodes)

    for search_term in range(min_edges, max_edges + 1):
        ccs = max_conn_comp(nodes, search_term)
        bridges = ccs - 1
        total_edges = bridges + search_term
        if bridges/total_edges >= 0.5:
            if total_edges > max_edges_found:
                max_edges_found = total_edges
                max_bridges_found = bridges
                total_edges = 0
    print("max_edges_found = %s" % max_edges_found)
    print("max_bridges_found = %s" % max_bridges_found)

    return ccs



def main():

    import sys

    data = [line.rstrip() for line in sys.stdin.readlines()]
    num_graphs = data[0]
    graph_sizes = [int(x) for x in data[1:]]

    for val in graph_sizes:
        print(binary_search(val))





if __name__ == '__main__':
    main()
