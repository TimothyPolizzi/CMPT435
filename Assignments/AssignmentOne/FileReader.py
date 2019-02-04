#!/usr/bin/env python

# A way to read a file of strings into an array

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"


# Reads a file
def read_file(path_to_file):
    file_to_read = open(path_to_file, "r")
    string_array = []

    error_check = file_to_read.readline()       # reads the first line of a file
    while error_check:                          # loop while there is another line to read
        string_array.append(error_check)        # add the string to the array
        error_check = file_to_read.readline()   # update the currently checked line
    return string_array
