# A merge sort for project2 of CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List


def quick_sort(to_sort: List[str]):
    """Quickly sorts a given list to_sort.

    Quick Sort picks an element as pivot and partitions the given array around the picked pivot. The important
    part to remember is that the upper bound must always be above the lower bound, as it will break if the two ever
    switch.

    Args:
        to_sort: The array to be sorted

    Returns:
        A sorted version of to_sort
    """
    temp_list = to_sort.copy()

    __quick_sort_helper(temp_list, 0, len(temp_list) - 1)

    return temp_list


def __quick_sort_helper(to_sort: List[str], low, high):
    if high > low:  # Should this method run?
        pivot = to_sort[low]
        left = low
        right = high

        while left <= right:  # Time to do some stuff
            while to_sort[left] < pivot:  # increment left until it has the number of spaces the pivot is from the left
                left = left + 1
            while to_sort[right] > pivot:  # same as the previous loop, but this time from the right
                right = right - 1

            if left <= right:  # if nothing has killed itself yet, swap the left and right items
                temp = to_sort[left]
                to_sort[left] = to_sort[right]
                to_sort[right] = temp

                left = left + 1
                right = right - 1

        __quick_sort_helper(to_sort, low, right)  # Insert brain damage here
        __quick_sort_helper(to_sort, left, high)
