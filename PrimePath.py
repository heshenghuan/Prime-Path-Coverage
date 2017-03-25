#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 2017

@author: heshenghuan (heshenghuan@sina.com)
http://github.com/heshenghuan
"""

import sys
import codecs as cs


def readGraphFromFile(src):
    """Read a graph structure from given file."""
    with cs.open(src, 'r', 'utf-8') as graphFile:
        # Read nodes set of graph
        graphFile.readline()
        nodes = [int(n) for n in graphFile.readline().split()]
        # Read initial nodes set of graph
        graphFile.readline()
        initNodes = [int(n) for n in graphFile.readline().split()]
        # Read end nodes set of graph
        graphFile.readline()
        endNodes = [int(n) for n in graphFile.readline().split()]
        # Read edges set of graph
        graphFile.readline()
        edges = {}
        for i in nodes:
            s = graphFile.readline().strip().split()
            if len(s) >= 1:
                edges[i] = [int(n) for n in s]
            else:
                edges[i] = []
        graph = {'nodes': nodes, 'init': initNodes,
                 'end': endNodes, 'edges': edges}
        return graph


def printGraph(graph):
    """Print a graph structure information."""
    print "Nodes:     ", graph['nodes']
    print "InitNodes: ", graph['init']
    print "EndNodes:  ", graph['end']
    print "Edges:"
    for n in graph['nodes']:
        print "%d to " % n, graph['edges'][n]


def findSimplePath(graph, exPaths, paths=[]):
    """Find the simple paths of a graph."""
    newExPaths = []
    for p in exPaths:
        # whether simple path's last node is not the end node
        if p[-1] not in graph['end']:
            # whether simple path's last node is the first node
            if p[-1] == p[0] and (len(p) - 1) >= 1:
                paths.append(p)
                continue
            # whether simple path has a inner loop
            if p[-1] in p[1:-1] and (len(p) - 1) >= 1:
                # there is a inner loop
                # without the last node it might be a prime path
                paths.append(p[:-1])
            else:
                for nx in graph['edges'][p[-1]]:
                    newExPaths.append(p + (nx, ))
        else:
            if (len(p) - 1) >= 1:
                paths.append(p)
    if len(newExPaths) > 0:
        findSimplePath(graph, newExPaths, paths)


def findPrimePaths(graph):
    """Find the prime paths of a graph."""
    exPaths = [(n, ) for n in graph['nodes']]
    simplePaths = []
    # recursively finding the simple paths of the graph
    findSimplePath(graph, exPaths, simplePaths)
    # sort the simple paths by length
    simplePaths = sorted(simplePaths, reverse=True, key=lambda a: len(a))
    # add the longest simple path to prime path
    primePaths = [", ".join(str(n) for n in simplePaths[0])]
    for p in simplePaths[1:]:
        p = ", ".join(str(n) for n in p)

        def isSubPath(x):
            """whether p is a subpath of exist prime paths"""
            return (p in x)

        # decide whether to add p to prime path
        # in py3 should import reduce first
        flag = map(isSubPath, primePaths)
        flag = reduce(lambda x, y: x or y, flag)
        if not flag:
            primePaths.append(p)

    print "Prime Paths of this graph(%d):" % len(primePaths)
    primePaths = sorted(primePaths, key=lambda a: (len(a), a))
    for i, p in enumerate(primePaths):
        print 'Path %2d: (%s)' % (i + 1, p)


def usage():
    print "Finding The Prime Paths."
    print "Please make sure the format of graph file is correct."
    print "The results cannot be guaranteed if the format is incorrect.\n",
    print "Usage: python PrimePath.py GRAPH"
    print "       GRAPH The file defined graph"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Arguments Error!"
        usage()
        sys.exit(-1)
    graphFile = sys.argv[1]
    graph = readGraphFromFile(graphFile)
    printGraph(graph)
    findPrimePaths(graph)
