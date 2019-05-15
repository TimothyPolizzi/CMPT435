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

    def bellman_ford_sssp(self, source: int):
        """ Bellman Ford single-sourced shortest path problem.

        Solves which path to a point in a graph is the fastest from a single point, and will determine if there is a
        negative-weight cycle that would cause there to be no minimum distance from points.

        Args:
            source: The starting single point to figure out all paths from.
        """
        distance = [inf] * len(self.vertex_list)
        predecessor = [None] * len(self.vertex_list)

        distance[source-1] = 0

        for i in range(len(self.vertex_list)):
            for edge in self.edge_list:
                vertex1_index = edge.vertex1-1
                vertex2_index = edge.vertex2-1

                if distance[vertex1_index] + edge.weight < distance[vertex2_index]:
                    distance[vertex2_index] = distance[vertex1_index] + edge.weight
                    predecessor[vertex2_index] = edge.vertex1

        for edge in self.edge_list:
            vertex1_index = edge.vertex1 - 1
            vertex2_index = edge.vertex2 - 1

            if distance[vertex1_index] + edge.weight < distance[vertex2_index]:
                print("Graph contains a negative-weight cycle")
                return
        self.__sssp_results(source, distance, predecessor)

    def __sssp_results(self, source: int, distance: List, predecessor: List):
        for i in range(len(distance)):
            print("{} -> {} cost is {};\tpath: {}".format(source, i+1, distance[i],
                                                          self.__path(source -1, i, predecessor)))

    def __path(self, source: int, goal: int, predecessor: List):
        """ Interprets the path from the output predecessor list

        Takes the output predecessor list from BellmanFord-sssp and interprets it into a string that follows the path
        that it would take to traverse to the element in the graph in the shortest path.

        Args:
            source: The original starting point of the Single Source Shortest Path
            goal: The final point in the path
            predecessor: The list of all previously traversed points from the Bellman Ford SSSP

        Returns:
            A string that contains the proper path from the source to the goal.
        """
        arrow = " -> "
        to_return = "{}".format(source + 1)
        incr = goal
        stack = [goal + 1]

        while incr != source:
            incr = predecessor[incr] - 1
            stack.append(incr + 1)

        stack.pop()  # this is to remove the excess start node

        for item in range(len(stack)):
            to_return = to_return + arrow + "{}".format(stack.pop())

        return to_return
