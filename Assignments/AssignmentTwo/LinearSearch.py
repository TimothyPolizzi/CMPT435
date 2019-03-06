# A linear search for CMPT 435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List


def linear_search(list_to_search: List[str], to_find: str) -> int:
    """A linear search method that searches list_to_sort for to_find.

    A way to exhaustively search an array list_to_sort to find the index of to_find in a linear fashion, that has O(n).

    Args:
        list_to_search(List[str]): The array of strings to search through.
        to_find(str): The string value that you are looking for in linear_search.

    Returns:
        The integer value of the index of to_find in list_to_search. Will return -1 if to_find is not in list_to_search.
    """
    i = 0

    while i < len(list_to_search) and list_to_search[i] != to_find:
        i = i + 1

    if i > len(list_to_search) - 1:
        i = -1

    return i
