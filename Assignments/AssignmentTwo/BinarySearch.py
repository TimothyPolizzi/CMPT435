# A binary search for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List
from typing import Tuple

comparisons = 0


def binary_search(to_search: List[str], to_find: str) -> Tuple[int, int]:
    """Searches through a sorted list to_search to find the string to_find.

    Goes through a sorted array to_search looking for the string to_find and returns its location when it finds it. If
    to_find is not in to_search, then this will return -1.

    Args:
        to_search(List[str]): The list of strings to be looked through.
        to_find(str): The string that is being looked for.

    Returns:
        The index in to_search that to_find is located at; -1 if to_find does not exist in to_search. Also returns
        the number of comparisons that it took to get the index.
    """

    if len(to_search) < 1:
        to_return = -1
    else:
        to_return = __binary_search(to_search, to_find, 0, len(to_search))

    print("Comparisons: " + str(comparisons))
    return to_return, comparisons


def __binary_search(to_search: List[str], to_find: str, start, stop) -> int:
    midpoint = int((start + stop) / 2)
    global comparisons

    if start <= stop:

        if to_search[midpoint] > to_find:
            comparisons = comparisons = 1
            to_return = __binary_search(to_search, to_find, start, midpoint-1)

        elif to_search[midpoint] < to_find:
            comparisons = comparisons + 1
            to_return = __binary_search(to_search, to_find, midpoint+1, stop)

        else:  # target is midpoint
            to_return = midpoint
    else:
        to_return = -1

    return to_return
