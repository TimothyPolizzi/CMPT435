#!/usr/bin/env python

# Project3 test code for CMPT435.

from Assignments.AssignmentThree.GraphMatrix import GraphMatrix


def main():
    test_graph()


def test_graph():
    test_matrix = GraphMatrix(5)
    test_matrix.add_edge(1, 2)
    test_matrix.add_edge(3, 4)
    test_matrix.add_edge(5, 5)
    test_matrix.print_matrix()
    

if __name__ == '__main__':
    main()

