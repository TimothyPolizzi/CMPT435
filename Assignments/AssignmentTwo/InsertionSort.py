# A insertion sort for project2 of CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List
from Assignments.AssignmentTwo.Swap import swap


def insertion_sort(to_sort: List[str]) -> List[str]:
    """Sorts a array to_sort using an insertion sort.

    Takes a number and checks if it is unsorted. If it is, goes through the unsorted part of the list
    and adds it in a sorted spot, maintaining the sorted part as always sorted.

    Args:
        to_sort(List[str]): The array of strings that is to be sorted.

    Returns:
        A sorted array of the strings in to_sort.
    """

    to_sort_copy = to_sort.copy()

    i = 0
    while i < to_sort_copy.__len__():
        j = i
        while j > 0 and to_sort_copy[j-1] > to_sort_copy[j]:
            swap(j-1, j, to_sort_copy)
            j = j - 1
        i = i + 1

    return to_sort_copy
