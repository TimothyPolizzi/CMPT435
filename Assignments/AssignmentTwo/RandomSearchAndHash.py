# A thing for project2 for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from Assignments.AssignmentOne.FileReader import read_file
from Assignments.AssignmentTwo.HashTable import HashTable
from Assignments.AssignmentTwo.BinarySearch import binary_search
from Assignments.AssignmentTwo.LinearSearch import linear_search
from Assignments.AssignmentTwo.QuickSort import quick_sort
from random import randint
from typing import List


def main():
    list_1 = read_file("../AssignmentOne/magicitems.txt")
    sorted_list = quick_sort(list_1)

    list_42 = get_42(list_1)
    binary(sorted_list, list_42)
    # linear(sorted_list, list_42)


def get_42(str_list: List[str]) -> List[str]:
    """Gets 42 random strings from magicitems.txt.

    42 pseudo-random items obtained from magicitems.txt.

    Args:
        str_list(List[str]): The list of strings to have 42 random items found.

    Returns:
        The list of the 42 pseudo-random strings.
    """
    items = []

    for i in range(42):
        to_add = str_list[randint(0, 665)]
        # print(str(i) + " " + to_add)
        items.append(to_add)

    return items


def binary(search_in: List[str], run_on: List[str]):
    """Searches for the index of each string in run_on.

    Args:
        run_on(List[str]): The list of strings to search.
        search_in(List[str]): The list of strings to search in.
    """
    for string in run_on:
        print(binary_search(search_in, string))


def linear(search_in: List[str], run_on: List[str]):
    """Searches for the index of each string in run_on.

    Args:
        run_on(List[str]): The list of strings to search.
        search_in(List[str]): The list of strings to search in.
    """
    for string in run_on:
        print(linear_search(search_in, string))


if __name__ == '__main__':
    main()
