# A thing for project2 for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from Assignments.AssignmentOne.FileReader import read_file
from Assignments.AssignmentTwo.HashTable import HashTable
from Assignments.AssignmentTwo.BinarySearch import binary_search
from Assignments.AssignmentTwo.LinearSearch import linear_search
from Assignments.AssignmentTwo.SelectionSort import selection_sort
from Assignments.AssignmentTwo.InsertionSort import insertion_sort
from Assignments.AssignmentTwo.MergeSort import merge_sort
from Assignments.AssignmentTwo.QuickSort import quick_sort
from random import randint
from typing import List
import math

alan_arbitrary_value = 42


def main():
    list_1 = read_file("../AssignmentOne/magicitems.txt")
    # print("Selection Sort: ")
    # selection_sort(list_1)
    # print("Insertion Sort: ")
    # insertion_sort(list_1)
    # print("Merge Sort: ")
    # merge_sort(list_1)
    print("Quick Sort: ")
    sorted_list = quick_sort(list_1)

    hash_tbl = HashTable()

    list_42 = get_42(list_1)
    # print("Linear Search:")
    # linear(sorted_list, list_42)
    # print("Binary Search:")
    # binary(sorted_list, list_42)

    add_all_to_table(hash_tbl, list_1)
    print(get_all_from_table(hash_tbl, list_42))


def get_42(str_list: List[str]) -> List[str]:
    """Gets 42 random strings from magicitems.txt.

    42 pseudo-random items obtained from magicitems.txt.

    Args:
        str_list(List[str]): The list of strings to have 42 random items found.

    Returns:
        The list of the 42 pseudo-random strings.
    """
    items = []

    for i in range(alan_arbitrary_value):
        to_add = str_list[randint(0, 665)]
        # print(str(i) + " " + to_add)
        items.append(to_add)

    return items


def binary(search_in: List[str], run_on: List[str]):
    """Searches for the index of each string in run_on.

    Args:
        run_on(List[str]): The list of strings to search.
        search_in(List[str]): The list of strings to search in.
    """
    comparisons = 0

    for string in run_on:
        tuple_result = binary_search(search_in, string)
        index = tuple_result[0]
        comparisons = comparisons + tuple_result[1]
        print(str(index))
    print("Average comparisons: " + str(math.ceil(comparisons / alan_arbitrary_value)))


def linear(search_in: List[str], run_on: List[str]):
    """Searches for the index of each string in run_on.

    Args:
        run_on(List[str]): The list of strings to search.
        search_in(List[str]): The list of strings to search in.
    """
    running_total = 0
    for string in run_on:
        index = linear_search(search_in, string)
        running_total = running_total + index
        print(str(index))
    print("Average comparisons: " + str(math.ceil(running_total / alan_arbitrary_value)))


def add_all_to_table(table: HashTable, list_to_add: List[str]):
    """Inserts all of list_to_add's items to table.

    Args:
        table(HashTable): The hash table that the items are to be inserted into.
        list_to_add(List[str]): The list of strings to be added to table.
    """
    for item in list_to_add:
        table.insert(item)


def get_all_from_table(table: HashTable, list_to_get: List[str]) -> List[str]:
    """Removes all of list_to_get from table and returns a list containing all the removed values.

    Args:
        table(HashTable): The hash table that is to have items removed from it.
        list_to_get(List[str]): The list of strings that is to be retrieved.

    Returns:
        A list containing all values removed from the table.
    """
    return_list = []
    comp_sum = 0

    for item in list_to_get:
        inner_list = table.get_list(table.calculate_hash(item))
        if inner_list is not None:
            print(item + ": [" + '; '.join(inner_list) + "]")
        else:
            print("None")

        removed_item = table.remove(item)
        print("Comparisons: " + str(table.comparisons))
        comp_sum = comp_sum + table.comparisons
        if removed_item is not None:
            return_list.append(removed_item.val)
        else:
            return_list.append(None)

    print("Avg Comparisons: " + str(math.ceil(comp_sum / len(list_to_get))))
    return return_list


if __name__ == '__main__':
    main()
