# My way of yoinking Alan's code from the graphs.txt file for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List
from Assignments.AssignmentThree.GraphMatrix import GraphMatrix


def main():
    # The variable below is the path to the graphs file, so that it can be read
    path = "/Users/timpolizzi/Downloads/graphs.txt"

    string_of_file = read_file(path)

    generate_matrix_graph(string_of_file)


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


def generate_matrix_graph(to_generate_with: List[str]):
    matrices = []

    for line in to_generate_with:
        if line.startswith("new"):
            matrices.append(GraphMatrix())
        elif line.startswith("add vertex"):
            to_add = int(line[len(line) - 1])
            print(to_add)
            matrices[len(matrices) - 1].add_vertex(to_add)
        elif line.startswith("add edge"):
            vertex_1 = int(line[len(line) - 5])  # TODO: Read in numbers of 2+ digits
            vertex_2 = int(line[len(line) - 1])
            print(vertex_1,  vertex_2)
            matrices[len(matrices) - 1].add_edge(vertex_1, vertex_2)


if __name__ == '__main__':
    main()

