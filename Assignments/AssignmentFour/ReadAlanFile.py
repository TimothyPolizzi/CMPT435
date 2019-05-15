# My way of yoinking Alan's code from the graphs.txt file for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List
# So I'm going to try and make this easier, I'll include the paths that work for you in a comment
# and then you can just comment out the ones I use and uncomment the ones that work on your device
from Assignments.AssignmentFour.LinkedWeightedGraph import LinkedWeightedGraph
# from LinkedWeightedGraph import LinkedWeightedGraph


def main():
    # The variable below is the path to the graphs file, so that it can be read
    graph_path = input("What is the path to the file? > ")

    string_of_file = read_file(graph_path)

    # show_read(string_of_file)

    generate_graph(string_of_file)


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


def show_read(to_print: List[str]):
    """ Shows if the items read in have been properly read

    Args:
        to_print: The list of strings that were read in
    """
    for string in to_print:
        print(string)


def generate_graph(to_generate_with: List[str]):

    lwg = []

    for line in to_generate_with:
        if line.startswith("new"):

            lwg.append(LinkedWeightedGraph())

        elif line.startswith("add vertex"):

            to_add = int(line.rsplit(' ', 1)[1])
            current_index = len(lwg) - 1

            lwg[current_index].add_vertex(to_add)

        elif line.startswith("add edge"):

            # Break down the string that contains the line into the numbers and not numbers as separate strings
            last_four = line.split(' ', 10)

            # Take the numbers in the list of strings and now we have the vertices
            vertex_1 = int(last_four[2])
            vertex_2 = int(last_four[4])
            weight = int(last_four[len(last_four)-1])

            current_index = len(lwg) - 1

            lwg[current_index].add_edge(weight, vertex_1, vertex_2)


def print_lists(*lists):
    for item in lists:
        for s_item in item:
            s_item.print_graph()
            print()


def print_traversals(traversals):
    for trav in traversals:
        trav.breadth_first_traversal(1)
        print()
        trav.depth_first_traversal(1)
        print()


if __name__ == '__main__':
    main()

