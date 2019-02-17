# A merge sort for project2 of CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List
from Assignments.AssignmentTwo.Swap import swap


def merge_sort(to_sort: List[str]) -> List[str]:
    """Sorts a list to_sort using a merge sort.

    Takes a list of strings and breaks them down into smaller lists of strings. Then takes those lists,
    compares them, and puts them back together in order. Every split is exactly half of the total number
    and the splits will split the list down into one string a piece.

    Args:
        to_sort(List[str]): The list of strings that is to be sorted.

    Returns:
        The sorted to_sort list.
    """

    to_sort_copy = to_sort.copy()
    __merge_sort_helper(to_sort_copy, 0, to_sort_copy.__len__())
    return to_sort_copy


def __merge_sort_helper(to_split: List[str], first_index: int, last_index: int):
    """Internal helper method, doc for me only

    First, find the middle of the list. Next up, recursively go through the right side of this list to find a
    single item, then go recursively go through the left hand side to get a single item. Finally smash them together
    and get the sorted (part of the) list.

    Args:
        to_split: The list that is to be split and sorted.
        first_index: The index of the first item in the list.
        last_index: The index of the last item in the list.
    """
    if first_index >= last_index:
        return to_split[first_index: last_index]

    middle = int((last_index - first_index) / 2)

    __merge_sort_helper(to_split, first_index, middle)
    __merge_sort_helper(to_split, middle, last_index)

    return __merge(to_split, first_index, middle, last_index)


def __merge(to_merge: List[str], first_index: int, mid_index: int, last_index: int):
    """Internal helper method, doc for me only

    Takes the list and goes through it, attempting to merge the items into order. Keeps placeholders for where
    the lists were merged and adds from one or the other depending on comparisons to the new list

    Args:
        to_merge:
        first_index:
        mid_index:
        last_index:
    """

    return_list = to_merge.copy()
    i = first_index
    internal_front = first_index
    internal_end = mid_index

    while i < last_index:
        if internal_end > internal_front and to_merge[internal_front] > to_merge[internal_end]:
            return_list[i] = to_merge[internal_end]
            internal_end = internal_end + 1
        else:
            return_list[i] = to_merge[internal_front]
            internal_front = internal_front + 1
        i = i + 1
    return return_list
