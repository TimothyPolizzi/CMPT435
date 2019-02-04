#!/usr/bin/env python

# A queue for project1 of CMPT435

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"

from myLinkedList import MyLinkedList


class MyQueue:
    def __init__(self):             # Initializes the queue
        self.inner_list = MyLinkedList()

    def enqueue(self, to_enqueue):  # Adds an item to the queue
        self.inner_list.add_to_end(to_enqueue)

    def dequeue(self):              # Removes an item from the queue
        removed_val = self.inner_list.remove_from_front()
        return removed_val
