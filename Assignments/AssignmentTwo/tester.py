#!/usr/bin/env python

# Project2 test code for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from Assignments.AssignmentOne.FileReader import read_file
from Assignments.AssignmentTwo.SelectionSort import selection_sort
from Assignments.AssignmentTwo.InsertionSort import insertion_sort
from Assignments.AssignmentTwo.MergeSort import merge_sort
from Assignments.AssignmentTwo.QuickSort import quick_sort
from Assignments.AssignmentTwo.LinearSearch import linear_search
from Assignments.AssignmentTwo.BinarySearch import binary_search
from Assignments.AssignmentTwo.HashTable import HashTable
from typing import List


def main():
    list_1 = read_file("../AssignmentOne/magicitems.txt")
    list_2 = ["a", "b", "c", "d", "e", "f", "g", "h"]
    list_3 = ["h", "g", "f", "e", "d", "c", "b", "a"]
    list_4 = []
    list_5 = ["e", "z", "b", "m", "e", "r", "k", "q"]

    # test_selection(list_1)
    # test_insertion(list_1)
    # test_merge(list_1)
    # test_quick(list_1)
    # # test_linear(list_1)
    # test_binary(list_1)
    # test_hash(list_1)


def test_selection(to_sort: List[str]):
    sorted_list = selection_sort(to_sort)
    print_list(sorted_list)


def test_insertion(to_sort: List[str]):
    sorted_list = insertion_sort(to_sort)
    print_list(sorted_list)


def test_merge(to_sort: List[str]):
    sorted_list = merge_sort(to_sort)
    print_list(sorted_list)


def test_quick(to_sort: List[str]):
    sorted_list = quick_sort(to_sort)
    print_list(sorted_list)


def test_linear(to_search: List[str]):
    print(linear_search(to_search, "axe"))
    print(linear_search(to_search, "a"))
    print(linear_search(to_search, "e"))


def test_binary(to_search: List[str]):
    sorted_list = quick_sort(to_search)

    print(binary_search(sorted_list, "axe"))
    print(binary_search(sorted_list, "a"))
    print(binary_search(sorted_list, "e"))


def test_hash(to_add: List[str]):
    test_table = HashTable()

    for item in to_add:
        test_table.insert(item)

    i = 0
    while i < 250:
        print(test_table.get_list(i))
        i = i + 1


def print_list(to_print: List[str]):
    for item in to_print:
        print(item)


if __name__ == '__main__':
    main()
