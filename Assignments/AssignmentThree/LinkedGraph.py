# A graph made of linked objects for Alan's CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List


class LinkedGraph(object):

    class __Node(object):
        """ An internal Node for the Linked Object model of the Graph

        """
        def __init__(self, set_id, *init_value):
            if 2 > len(init_value) > 0:
                self.value = init_value
            else:
                self.value = None
            self.connected_nodes = []
            self.id = set_id

        def connect(self, node):
            self.connected_nodes.append(node)

        def set_value(self, value: int):
            self.value = value

    def __init__(self):
        self.vertex_list = []

    def add_vertex(self, to_add):
        """ Adds a vertex to the graph.

        Args:
            to_add: The value of the vertex to add.

        Returns:
            A boolean value that returns True if it worked, False otherwise.
        """
        to_return = True

        self.vertex_list.append(self.__Node(len(self.vertex_list), to_add))

        return to_return

    def find_node(self, to_find) -> __Node:
        """ Finds a node in the graph based on it's value.

        Args:
            to_find: The integer value of the node that is being searched for.

        Returns:
            The node who's value corresponds to the integer value queried, or None if the node could not be found.
        """
        to_return = None

        for node in self.vertex_list:
            if node.value[0] is to_find:
                to_return = node

        return to_return

    def add_edge(self, vertex_1, vertex_2):
        """ Adds an edge between two vertices to the graph.

        Args:
            vertex_1: The first vertex to be connected.
            vertex_2: The second vertex to be connected.

        Returns:
            A boolean value that is True if the edge is created, False otherwise.
        """
        to_return = True

        temp1 = self.find_node(vertex_1)
        temp2 = self.find_node(vertex_2)

        temp1.connected_nodes.append(temp2)
        temp2.connected_nodes.append(temp1)

        return to_return

    def breadth_first_traversal(self, start: int):
        """ A breadth first traversal through the graph.

        A way to traverse the graph, by moving from one node to all adjacent nodes, before moving on to do the process
        again.

        Args:
            start: The node to start the traversal on.

        Returns:
            The list of traversed nodes in breadth first order.
        """
        visited = [False] * len(self.vertex_list)
        begin = self.find_node(start)

        queue = [begin]
        visited[begin.id] = True
        traverse_list = [begin]

        while queue:
            begin = queue.pop(0)
            print(begin.value[0], end=" ")

            for i in begin.connected_nodes:
                if not visited[i.id]:
                    queue.append(i)
                    visited[i.id] = True
                    traverse_list.append(i)
        print()
        return traverse_list

    def depth_first_traversal(self, start: int):
        """ A depth first traversal through the graph.

        A way to traverse the graph, by moving from one node to the next child node, until there are no further children
        when it goes back up a step to continue in the other direction for child nodes.

        Args:
            start: The index of the node to start the traversal on.

        Returns:
            The list of items that have been traversed.
        """
        visited = [False] * len(self.vertex_list)
        traverse_list = []

        self.__depth_first_traversal_helper(start - 1, visited, traverse_list)
        print()
        return traverse_list

    def __depth_first_traversal_helper(self, start: int, visited: List[bool], traverse_list: List[int]):
        visited[start-1] = True
        traverse_list.append(start)
        print(start + 1, end=" ")

        start_node = self.vertex_list[start]

        for i in start_node.connected_nodes:
            if not visited[i.id - 1]:
                self.__depth_first_traversal_helper(i.id, visited, traverse_list)
