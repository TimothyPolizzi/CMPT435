#!/usr/bin/env python

# A linked list written for the intention of making it into a stack or queue

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"


class TextNode:                     # Nodes, that have a string stored in them
    def __init__(self, *args):      # Constructor
        if len(args) == 0:          # Constructor for an empty call of TextNode
            self.val = ""
            self.next = ""
        elif len(args) == 2:        # Constructor for TextNode with predefined text and next node
            internal_text = args[0]
            next_node = args[1]
            self.val = internal_text
            self.next = next_node


class MyLinkedList:                 # A linked list that i've made
    def __init__(self):
        self.head = None

    def traverse(self, *args):
        if not self.is_empty():
            current_node = self.head

            if len(args) == 1:      # Traversal to find a particular TextNode
                text_to_visit = args[0]
                while current_node.val is not text_to_visit:
                    current_node = current_node.next
            elif len(args) == 0:    # Traversal to find the last node in the list
                    while current_node.next is not None:
                        current_node = current_node.next
        else:
            current_node = None

        return current_node

# checks if the list is empty
    def is_empty(self):
        to_return = False
        if self.head is None:
            to_return = True
        return to_return

# Add a node to the front
    def add_to_front(self, text):
        new_node = TextNode(text, self.head)
        self.head = new_node

# Add a node to the end
    def add_to_end(self, text):
        new_node = TextNode(text, None)
        if self.is_empty():
            self.head = new_node
        else:
            last_node = self.traverse()
            last_node.next = new_node

# Remove a node from the front
    def remove_from_front(self):
        if self.is_empty():
            raise Exception('List is empty')
        else:
            old_head_val = self.head.val
            self.head = self.head.next
            return old_head_val
