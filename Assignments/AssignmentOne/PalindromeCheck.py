#!/usr/bin/env python

# Project1 for CMPT435.

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"

from Assignments.AssignmentOne.MyStack import MyStack
from Assignments.AssignmentOne.MyQueue import MyQueue
from Assignments.AssignmentOne.FileReader import read_file
import re
import typing


def main():
    # Change this filepath to wherever the file you want to check is.
    check_file_for_palindromes("magicitems.txt")


def string_cleaner(string_to_clean: str, regex: typing.Pattern) -> str:
    """Cleans a string that is to be checked if it is a palindrome.

    Takes a string and removes any non-alphabet characters from it.

    Args:
        string_to_clean(String): The string that is to have any non-alphabetic characters removed from it.
        regex(re): A compiled regex used to clean the string.

    Returns:
        string_to_clean after it has had all non-alphabetic characters removed from it.
    """
    updated_string_to_clean = string_to_clean[0:-1].lower()  # This removes the annoying little \n tag

    # I didn't want to use an external library but I REALLY did not want to write all those elifs

    final_cleaned_string = regex.sub('', updated_string_to_clean)  # Put it all back together
    return final_cleaned_string


def check_for_palindrome(string_to_check: str) -> bool:
    """Checks a string to see if it is a palindrome.

    Takes a string and checks to see if the spelling is the same going forward as it is backward.

    Args:
        string_to_check(String): The string that is to be checked to see if it is a palindrome.

    Returns:
        A bool that is True if string_to_check is a palindrome, False otherwise.
    """
    character_list = list(string_to_check)

    stack = MyStack()
    queue = MyQueue()

    for character in character_list:
        stack.push(character)
        queue.enqueue(character)

    counter = 0
    stack_and_queue_are_equal = True
    # just check that there if the last letter has been hit or if the stack and queue don't match
    # (cuz they aren't palindromes if they don't match)
    while counter < character_list.__len__() and stack_and_queue_are_equal:
        counter += 1
        stack_char = stack.pop()
        queue_char = queue.dequeue()
        stack_and_queue_are_equal = stack_char is queue_char

    return stack_and_queue_are_equal


def check_file_for_palindromes(file_to_read: str):
    """Takes a text file and checks if any of the words in it are palindromes.

    Takes a given file and scans it of all words, then checks each word individually to see if is a palindrome.
    If a palindrome is found, the palindrome will be printed in the terminal.

    Args:
        file_to_read(String): The path to the file to be checked for palindromes.
    """
    regex = re.compile('[^a-zA-Z]')
    array_of_strings = read_file(file_to_read)
    for string in array_of_strings:
        corrected_string = string_cleaner(string, regex)
        if check_for_palindrome(corrected_string):
            print(string)


if __name__ == '__main__':
    main()
