#!/usr/bin/env python

# Project1 for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from Assignments.AssignmentOne.FileReader import read_file
from Assignments.AssignmentTwo.SelectionSort import selection_sort
from typing import List


def main():
    to_sort_1 = read_file("../AssignmentOne/magicitems.txt")
    to_sort_2 = ["a", "b", "c", "d", "e", "f", "g", "h"]
    to_sort_3 = ["h", "g", "f", "e", "d", "c", "b", "a"]
    to_sort_4 = []
    to_sort_5 = ["e", "z", "b", "m", "e", "r", "k", "q"]

    test_selection(to_sort_1)


def test_selection(to_sort: List[str]):
    sorted_list = selection_sort(to_sort)

    for item in sorted_list:
        print(item)


if __name__ == '__main__':
    main()
