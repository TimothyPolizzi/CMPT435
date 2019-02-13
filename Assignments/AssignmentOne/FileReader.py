# A way to read a file of strings into an array.

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"

from typing import List


def read_file(path_to_file: str) -> List[str]:
    """Reads a text file into an array.

    Reads each line of a text file into entries in an array.

    Args:
        path_to_file(String): The string path to the file that is to be read.

    Returns:
        List[str]: The array of strings that contain the lines of the file that was read.
    """
    file_to_read = open(path_to_file, "r")
    string_array = []

    error_check = file_to_read.readline()  # reads the first line of a file
    while error_check:  # loop while there is another line to read
        error_check = error_check[0:-1].lower()  # This removes the annoying little \n tag
        string_array.append(error_check)  # add the string to the array
        error_check = file_to_read.readline()  # update the currently checked line
    return string_array
