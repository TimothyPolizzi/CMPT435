# An adjacency list format for a graph Alan's for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'


class AdjacencyList(object):

    def __init__(self):
        self.inner_list = []  # A list that contains sub-lists

    def add_vertex(self, vertex_to_add: int):
        """ Adds a new vertex with given index.

        Args:
            vertex_to_add: The index of the vertex to be added.

        Returns:
            A boolean value that is True if the addition of the vertex works, false otherwise.
        """
        return_bool = True

        self.inner_list.append([])

        return return_bool

    def add_edge(self, vertex_1: int, vertex_2: int):
        """ Adds a new edge between two vertices.

        Args:
            vertex_1: One edge to be connected.
            vertex_2: The second edge to be connected.

        Returns:
            A boolean value that is True if the addition of the edge works, false otherwise.
        """

        return_bool = True

        self.inner_list[vertex_1-1].append(vertex_2)
        self.inner_list[vertex_2-1].append(vertex_1)

        return return_bool

    def print_graph(self):
        """ Prints the graph out.

        Returns:
            A boolean value that is true if the graph successfully printed, false otherwise.
        """

        return_bool = True

        for i in self.inner_list:
            print(self.inner_list.index(i) + 1, end=" ")
            for j in i:
                print(j, end=" ")
            print()

        return return_bool
