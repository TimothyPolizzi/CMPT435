# A merge sort for project2 of CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List


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
    to_sort_copy = __merge_sort_helper(to_sort_copy)
    return to_sort_copy


def __merge_sort_helper(to_split: List[str]) -> List[str]:
    """Internal helper method, doc for me only

    First, find the middle of the list. Next up, recursively go through the right side of this list to find a
    single item, then go recursively go through the left hand side to get a single item. Finally smash them together
    and get the sorted (part of the) list.

    Args:
        to_split(List[str]): The list that is to be split and sorted.

    Returns:
        The sorted list to_split.
    """
    if len(to_split) <= 1:
        return to_split

    middle = int(len(to_split) / 2)

    left = __merge_sort_helper(to_split[:middle])
    right = __merge_sort_helper(to_split[middle:])

    return __merge(left, right)


def __merge(left: List[str], right: List[str]):
    """Internal helper method, doc for me only

    Takes the list and goes through it, attempting to merge the items into order. Keeps placeholders for where
    the lists were merged and adds from one or the other depending on comparisons to the new list.

    Args:
        left(List[str]): The sorted left half of the list.
        right(List[str]): The sorted right half of the list.

    Returns:
        A sorted list of both left and right.
    """

    left_index = 0
    right_index = 0
    result = []

    # While there are things in either list loop.
    while left_index < len(left) and right_index < len(right):
        # If the current item in the left list is less than that of the right list.
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index = left_index + 1
        else:
            result.append(right[right_index])
            right_index = right_index + 1

    # Once the left or right side has run out of items, dump the rest into the return list.
    result = result + left[left_index:]
    result = result + right[right_index:]
    return result
