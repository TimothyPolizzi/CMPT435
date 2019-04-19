#!/usr/bin/env python

# Project3 test code for CMPT435.

from Assignments.AssignmentThree.GraphMatrix import GraphMatrix
from Assignments.AssignmentThree.AdjacencyList import AdjacencyList
from Assignments.AssignmentThree.LinkedGraph import LinkedGraph
from Assignments.AssignmentThree.BinarySearchTree import BinarySearchTree


def main():
    # test_matrix()
    # test_adjacency()
    # test_nodes_breadth()
    # test_nodes_depth()
    test_bst()


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


def test_nodes_breadth():
    test_node = LinkedGraph()
    test_node.add_vertex(1)
    test_node.add_vertex(2)
    test_node.add_vertex(3)
    test_node.add_vertex(4)
    test_node.add_vertex(5)
    test_node.add_vertex(6)
    test_node.add_vertex(7)
    test_node.add_edge(1, 2)
    test_node.add_edge(1, 5)
    test_node.add_edge(2, 3)
    test_node.add_edge(2, 4)
    test_node.add_edge(5, 6)
    test_node.add_edge(5, 7)
    test_node.breadth_first_traversal(1)


def test_nodes_depth():
    test_node = LinkedGraph()
    test_node.add_vertex(1)
    test_node.add_vertex(2)
    test_node.add_vertex(3)
    test_node.add_vertex(4)
    test_node.add_vertex(5)
    test_node.add_vertex(6)
    test_node.add_vertex(7)
    test_node.add_edge(1, 2)
    test_node.add_edge(1, 5)
    test_node.add_edge(2, 3)
    test_node.add_edge(2, 4)
    test_node.add_edge(5, 6)
    test_node.add_edge(5, 7)
    test_node.depth_first_traversal(1)


def test_bst():
    bst = BinarySearchTree()
    bst.add("a")
    bst.add("b")
    bst.add("d")
    bst.add("c")
    bst.add("e")
    bst.add("z")
    bst.add("a")
    bst.add("f")
    print(bst.depth_first_traversal())
    print(bst.breadth_first_traversal())


if __name__ == '__main__':
    main()

