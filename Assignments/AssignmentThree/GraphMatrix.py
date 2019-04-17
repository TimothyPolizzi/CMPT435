# An implementation of a graph in matrix format for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'


class GraphMatrix(object):

    def __init__(self):
        self.inner_list = []

    def add_vertex(self, vertex_num: int):
        self.inner_list.append([])

    def add_edge(self, vertex_1: int, vertex_2: int):
        """ Adds an edge to the graph between two vertices.

        Adds a logical edge to the graph to link two vertices.

        Args:
            vertex_1(int): The first vertex that is to be linked
            vertex_2(int): The second vertex that is to be linked

        Returns:
            A boolean value that is true if it worked, or false if it did not.
        """
        to_return = False
        vert_1 = vertex_1 - 1
        vert_2 = vertex_2 - 1

        if 0 <= vert_1 < len(self.inner_list) and 0 <= vert_2 < len(self.inner_list[vert_1]):
            self.inner_list[vert_1][vert_2] = "O"
            self.inner_list[vert_2][vert_1] = "O"
            to_return = True

        return to_return

    def print_matrix(self):
        """ Prints out the matrix

            Prints the matrix out in a simple square format.
        """
        for i in self.inner_list:
            for j in i:
                print(j, end=" ")
            print()
