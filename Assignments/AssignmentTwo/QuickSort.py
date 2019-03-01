# A merge sort for project2 of CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List
import random


def quick_sort(to_sort: List[str]) -> List[str]:
    """Quickly sorts a given list to_sort.

    Quick Sort picks an element as pivot and partitions the given array around the picked pivot. Next it recursively
    does this down to the smallest elements. Have the partitions and the values in a tree and then to find the final
    answer, just take the leaf nodes and print them.

    Args:
        to_sort: The array to be sorted

    Returns:
        A sorted version of to_sort
    """

    if len(to_sort) <= 1:
        return

    temp_list = to_sort.copy()
    pivot = temp_list[random.randint(0, len(temp_list))]

    left_list = []
    right_list = []
    iter_no = 0

# it is possible to do this in place, which is absolutely insane bc n log n time with constant storage
    for item in temp_list:
        if item < pivot:
            left_list[iter_no] = item
        else:
            right_list[iter_no] = item
        iter_no = iter_no + 1

    sorted_left = quick_sort(left_list)
    sorted_right = quick_sort(right_list)

    nice_array = [sorted_left, pivot, sorted_right]

    return nice_array
