# My way of yoinking Alan's code from the graphs.txt file for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List
import random
from Assignments.AssignmentThree.GraphMatrix import GraphMatrix
from Assignments.AssignmentThree.AdjacencyList import AdjacencyList
from Assignments.AssignmentThree.LinkedGraph import LinkedGraph
from Assignments.AssignmentThree.BinarySearchTree import BinarySearchTree


def main():
    # The variable below is the path to the graphs file, so that it can be read
    graph_path = "/Users/timpolizzi/Downloads/graphs.txt"
    magic_path = "/Users/timpolizzi/Downloads/magicitems.txt"

    string_of_file = read_file(graph_path)
    string_of_items = read_file(magic_path)

    generate_graph(string_of_file)
    tree = generate_tree(string_of_items)

    test_tree(tree, string_of_items)


def read_file(path_to_file: str) -> List[str]:
    """Reads a text file into an array.

    Reads each line of a text file into entries in an array.

    Args:
        path_to_file(String): The string path to the file that is to be read.

    Returns:
        List[str]: The array of strings that contain the lines of the file that was read.
    """
    file_to_read = open(path_to_file, 'r')
    string_array = []

    error_check = file_to_read.readline()  # reads the first line of a file
    # loop while there is another line to read and the line is not a comment
    while error_check:
        if error_check[0] != '-':
            error_check = error_check[0:-1].lower()  # This removes the annoying little \n tag
            string_array.append(error_check)  # add the string to the array
            error_check = file_to_read.readline()  # update the currently checked line
        else:
            error_check = file_to_read.readline()
    return string_array


def generate_graph(to_generate_with: List[str]):
    matrices = []
    adj_lists = []
    node_graph = []

    for line in to_generate_with:
        if line.startswith("new"):

            matrices.append(GraphMatrix())
            adj_lists.append(AdjacencyList())
            node_graph.append(LinkedGraph())

        elif line.startswith("add vertex"):

            to_add = int(line.rsplit(' ', 1)[1])
            current_index = len(matrices) - 1

            matrices[current_index].add_vertex(to_add)
            adj_lists[current_index].add_vertex(to_add)
            node_graph[current_index].add_vertex(to_add)

        elif line.startswith("add edge"):

            # Break down the string that contains the line into the numbers and not numbers as separate strings
            last_three = line.rsplit(' ', 3)

            # Take the numbers in the list of strings and now we have the vertices
            vertex_1 = int(last_three[1])
            vertex_2 = int(last_three[3])

            current_index = len(matrices) - 1

            if not matrices[current_index].filled:
                matrices[current_index].fill_matrix()
            matrices[current_index].add_edge(vertex_1, vertex_2)

            adj_lists[current_index].add_edge(vertex_1, vertex_2)

            node_graph[current_index].add_edge(vertex_1, vertex_2)

    print_lists(matrices, adj_lists)
    print_traversals(node_graph)


# This was a mistake, trust me, but its working so idc
def print_lists(*lists):
    for item in lists:
        for s_item in item:
            s_item.print_graph()
            print()


def generate_tree(to_generate_with: List[str]):
    bst = BinarySearchTree()

    for item in to_generate_with:
        bst.add(item)

    return bst


def test_tree(tree: BinarySearchTree, item_list: List[str]):
    for i in range(42):
        rand = random.randint(1, 666)
        tree.contains(item_list[rand])
    print("\n", tree.comp_total / 42)


def print_traversals(traversals):
    for trav in traversals:
        trav.breadth_first_traversal(1)
        print()
        trav.depth_first_traversal(1)
        print()


if __name__ == '__main__':
    main()

