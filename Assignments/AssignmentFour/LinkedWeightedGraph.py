# A graph made of linked objects for Alan's CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List
from math import inf


class LinkedWeightedGraph(object):

    class __Vertex(object):
        """ An internal Node for the Linked Object model of the Graph

        """
        def __init__(self, set_id, *init_value):
            if 2 > len(init_value) > 0:
                self.value = init_value
            else:
                self.value = None
            self.edges = []
            self.id = set_id

        def connect(self, edge):
            self.edges.append(edge)

    class __Edge(object):
        def __init__(self, set_weight: int, vertex1, vertex2):
            self.weight = set_weight
            self.vertex1 = vertex1
            self.vertex2 = vertex2

    def __init__(self):
        self.vertex_list = []
        self.edge_list = []

    def add_vertex(self, to_add):
        """ Adds a vertex to the graph.

        Args:
            to_add: The value of the vertex to add.

        Returns:
            A boolean value that returns True if it worked, False otherwise.
        """
        to_return = True

        self.vertex_list.append(self.__Vertex(len(self.vertex_list), to_add))

        return to_return

    def find_node(self, to_find) -> __Vertex:
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

    def add_edge(self, weight: int, vertex_1: __Vertex, vertex_2: __Vertex):
        """ Adds an edge between two vertices to the graph.

        Args:
            vertex_1: The first vertex to be connected.
            vertex_2: The second vertex to be connected.
            weight: The weight of the edge connecting vertex_1 and vertex_2

        Returns:
            A boolean value that is True if the edge is created, False otherwise.
        """
        to_return = True

        temp1 = self.find_node(vertex_1)
        temp2 = self.find_node(vertex_2)

        temp1.edges.append(temp2)
        temp2.edges.append(temp1)

        self.edge_list.append(self.__Edge(weight, vertex_1, vertex_2))

        return to_return

    def BellmanFord_sssp(self, source: __Vertex):
        """ Bellman Ford single-sourced shortest path problem.

        Args:
            source:

        Returns:

        """
        distance = []
        predecessor = []

        for vertex in range(len(self.vertex_list)):
            distance[vertex] = inf
            predecessor[vertex] = None

            if self.vertex_list[vertex] == source:
                distance[vertex] = 0

        for i in range(len(self.vertex_list)):
            for edge in self.edge_list:
                if distance[edge.vertex1] + edge.weight < distance[edge.vertex2]:
                    distance[edge.vertex2] = distance[edge.vertex1] + edge.weight
                    predecessor[edge.vertex2] = edge.vertex1

        for edge in self.edge_list:
            if distance[edge.vertex2] + edge.weight < distance[edge.vertex1]:
                print("Graph contains a negative-weight cycle")
                return
