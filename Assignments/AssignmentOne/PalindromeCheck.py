#!/usr/bin/env python

# Project1 for CMPT435

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"

from myStack import MyStack
from myQueue import MyQueue
from FileReader import read_file
import re


# clean up that hellish string (ew, +4 gear?) that i pull from whatever text file is supplied
def string_cleaner(string_to_clean):
    updated_string_to_clean = string_to_clean[0:-1].lower()
    regex = re.compile('[^a-zA-Z]')         # long story short, I didn't wanna elif the alphabet
    final_cleaned_string = regex.sub('', updated_string_to_clean)
    return final_cleaned_string


# check a string to see if its a palindrome. This doesn't care what goes in, clean or not
def check_for_palindrome(string_to_check):
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


# run my check for palindromes on a file who's path has been supplied
def check_file_for_palindromes(file_to_read):
    array_of_strings = read_file(file_to_read)
    for string in array_of_strings:
        corrected_string = string_cleaner(string)
        if check_for_palindrome(corrected_string):
            print(string)


check_file_for_palindromes()
