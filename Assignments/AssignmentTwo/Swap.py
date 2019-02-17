# A swap method

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List


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
