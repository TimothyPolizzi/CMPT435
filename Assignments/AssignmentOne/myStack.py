#!/usr/bin/env python

# A stack for project1 of CMPT435

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"

from myLinkedList import MyLinkedList


class MyStack:
    def __init__(self):  # Initializes the Stack
        self.inner_list = MyLinkedList()

    def push(self, to_push):  # Adds an item to the stack
        self.inner_list.add_to_front(to_push)

    def pop(self):  # Removes an item from the stack
        popped_node = self.inner_list.remove_from_front()
        return popped_node

    def peek(self):  # Looks at the top item from the stack without removing it
        peek_val = self.pop()
        self.push(peek_val)
        return peek_val
