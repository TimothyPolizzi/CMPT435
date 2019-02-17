# A Selection Sort for project2 of CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List
from Assignments.AssignmentTwo.Swap import swap


def selection_sort(to_sort: List[str]) -> List[str]:
    """Sorts an array to_sort using a selection sort.

    Sorts an array by having a sorted portion of the array and an unsorted portion. The sort takes the
    items in the unsorted portion and finds the smallest, then swaps it with the next item after the
    sorted portion. This continues until the sorted portion is the last item in the array.

    Args:
        to_sort(List): The list of items that are to be sorted.

    Returns:
        A new list containing the sorted array.
    """
    to_sort_copy = to_sort.copy()

    i = 0
    while i < (to_sort_copy.__len__() - 1):

        # print(i)
        j = i + 1
        current_smallest = i

        while j < (to_sort_copy.__len__()):

            # print(j)
            # print(to_sort_copy[current_smallest])
            # print(to_sort_copy[j])
            # print(to_sort_copy[current_smallest] > to_sort_copy[j])
            if to_sort_copy[current_smallest] > to_sort_copy[j]:

                current_smallest = j

            j = j + 1

        swap(current_smallest, i, to_sort_copy)
        i = i + 1

    return to_sort_copy
