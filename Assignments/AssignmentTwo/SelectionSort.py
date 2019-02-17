# A stack for project1 of CMPT435. Also for fun.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List


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


def swap(item1: int, item2: int, arr: List):
    """Swaps the position of two items in an array.

    Taken two integers (item1 and item2), swaps the values of whatever is at
    their positions in the array.

    Args:
        item1(int): The index of whatever the first item to swap is.
        item2(int): The index of whatever the second item to swap is.
        arr(List): The array that is to have the items swapped in.
    """

    temp_store = arr[item1]
    arr[item1] = arr[item2]
    arr[item2] = temp_store
