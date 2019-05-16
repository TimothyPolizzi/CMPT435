# My way of yoinking Alan's code from the graphs.txt file for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List
# So I'm going to try and make this easier, I'll include the paths that work for you in a comment
# and then you can just comment out the ones I use and uncomment the ones that work on your device
# from Assignments.AssignmentFour.LinkedWeightedGraph import LinkedWeightedGraph
from LinkedWeightedGraph import LinkedWeightedGraph
# from Assignments.AssignmentFour.Melange import Melange
from Melange import Melange
# from Assignments.AssignmentFour.FractionalKnapsack import FractionalKnapsack
from FractionalKnapsack import FractionalKnapsack


def main():
    # The variable below is the path to the graphs file, so that it can be read
    graph_path = input("What is the path to the file? > ")

    # lazy = "/Users/timpolizzi/Downloads/spice.txt"

    string_of_file = read_file(graph_path)  # change to graph_path on final run

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
    """Takes in the list of strings to_generate_with and produces stuff.

    (stuff is specifically a graph and a knapsack in this case)

    Args:
        to_generate_with: A list of strings taken in from some external file by read_file
    """

    lwg = []
    spice_list = []

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

        elif line.startswith("spice"):

            spice_attrs = line.split(' ', 20)
            spice_attrs_right = line.rsplit(' ', 8)

            name = spice_attrs[3]
            name = name[:len(name)-1]

            price = spice_attrs_right[4]
            price = float(price[:len(price)-1])

            qty = spice_attrs_right[8]
            qty = int(qty[:len(qty)-1])

            spice_list.append(Melange(name, price, qty))

        elif line.startswith("knapsack"):
            capacity = line.rsplit(' ', 2)[2]
            capacity = int(capacity[:len(capacity)-1])

            knapsack = FractionalKnapsack(capacity)
            knapsack_print(knapsack, spice_list)

    print_traversals(lwg)


def print_traversals(traversals):
    for trav in traversals:
        trav.bellman_ford_sssp(1)
        print()


def knapsack_print(knapsack: FractionalKnapsack, spice_list: List):
    for spice in spice_list:
        knapsack.add_spice(spice)
    knapsack.fill_bag()
    filled_with_str = ""

    for spice in knapsack.filled_with:
        filled_with_str = filled_with_str + " " + spice.name

    print("Filled with{}; price: {}".format(filled_with_str, knapsack.total_value))


if __name__ == '__main__':
    main()

