#!/usr/bin/env python

# Project3 test code for CMPT435.

from Assignments.AssignmentThree.GraphMatrix import GraphMatrix
from Assignments.AssignmentThree.AdjacencyList import AdjacencyList


def main():
    # test_matrix()
    test_adjacency()


def test_adjacency():
    test_adj = AdjacencyList()
    test_adj.add_vertex(1)
    test_adj.add_vertex(2)
    test_adj.add_vertex(3)
    test_adj.add_vertex(4)
    test_adj.add_vertex(5)
    test_adj.add_edge(1, 2)
    test_adj.add_edge(3, 4)
    test_adj.add_edge(5, 5)
    test_adj.print_graph()


def test_matrix():
    test_matrix1 = GraphMatrix()
    test_matrix1.add_vertex(1)
    test_matrix1.add_vertex(2)
    test_matrix1.add_vertex(3)
    test_matrix1.add_vertex(4)
    test_matrix1.add_vertex(5)
    test_matrix1.fill_matrix()
    test_matrix1.add_edge(1, 2)
    test_matrix1.add_edge(3, 4)
    test_matrix1.add_edge(5, 5)
    test_matrix1.print_graph()
    

if __name__ == '__main__':
    main()

