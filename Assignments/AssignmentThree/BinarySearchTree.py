# A binary search tree for Alan's CMPT435 class.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from Assignments.AssignmentThree.LinkedGraph import LinkedGraph


class BinarySearchTree(object):
    def __init__(self):
        self.inner_graph = LinkedGraph()
        self.head = None

    def add(self, to_add: str):
        if self.head is None:
            self.inner_graph.add_vertex(to_add)
            self.head = to_add


