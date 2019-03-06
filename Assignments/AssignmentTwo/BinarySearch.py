# A binary search for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List


def binary_search(to_search: List[str], to_find: str) -> int:
    """Searches through a sorted list to_search to find the string to_find.

    Goes through a sorted array to_search looking for the string to_find and returns its location when it finds it. If
    to_find is not in to_search, then this will return -1.

    Args:
        to_search(List[str]): The list of strings to be looked through.
        to_find(str): The string that is being looked for.

    Returns:
        The index in to_search that to_find is located at; -1 if to_find does not exist in to_search.
    """
    return __binary_search(to_search, to_find, 0, len(to_search))


def __binary_search(to_search: List[str], to_find: str, start, stop) -> int:
    midpoint = int((start + stop) / 2)

    if start > stop or stop == 0:
        return -1

    if to_search[midpoint] > to_find:
        return __binary_search(to_search, to_find, start, midpoint-1)
    elif to_search[midpoint] < to_find:
        return __binary_search(to_search, to_find, midpoint+1, stop)
    else:  # target is midpoint
        return midpoint
