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
                edges[i] = [int(n) for n in s if n != '-1']
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


def isPrimePath(path, graph):
    """Whether a path is a prime path."""
    if len(path) >= 2 and path[0] == path[-1]:
        return True
    elif reachHead(path, graph) and reachEnd(path, graph):
        return True
    else:
        return False


def reachHead(path, graph):
    """
    Whether the path can be extended at head, and the extended path is still
    a simple path.
    """
    former_nodes = filter(lambda n: path[0] in graph[
                          'edges'][n], graph['nodes'])
    for n in former_nodes:
        if n not in path or n == path[-1]:
            return False
    return True


def reachEnd(path, graph):
    """
    Whether the path can be extended at tail, and the extended path is still
    a simple path.
    """
    later_nodes = graph['edges'][path[-1]]
    for n in later_nodes:
        if n not in path or n == path[0]:
            return False
    return True


def extendable(path, graph):
    """Whether a path is extendable."""
    if isPrimePath(path, graph) or reachEnd(path, graph):
        return False
    else:
        return True


def findSimplePath(graph, exPaths, paths=[]):
    """Find the simple paths of a graph."""
    paths.extend(filter(lambda p: isPrimePath(p, graph), exPaths))
    exPaths = filter(lambda p: extendable(p, graph), exPaths)
    newExPaths = []
    for p in exPaths:
        for nx in graph['edges'][p[-1]]:
            if nx not in p or nx == p[0]:
                newExPaths.append(p + (nx, ))
    if len(newExPaths) > 0:
        findSimplePath(graph, newExPaths, paths)


def findPrimePaths(graph):
    """Find the prime paths of a graph."""
    exPaths = [(n, ) for n in graph['nodes']]
    simplePaths = []
    # recursively finding the simple paths of the graph
    findSimplePath(graph, exPaths, simplePaths)
    primePaths = sorted(simplePaths, key=lambda a: (len(a), a))
    print len(primePaths)
    for p in primePaths:
        print list(p)


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
    # printGraph(graph)
    findPrimePaths(graph)
