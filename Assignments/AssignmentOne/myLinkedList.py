#!/usr/bin/env python

# A linked list written for the intention of making it into a stack or queue

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"


class TextNode:  # Nodes, that have a string stored in them
    def __init__(self):
        self.val = ""
        self.next = ""

    def __init__(self, text, next_node):
        self.val = text
        self.next = next_node


class MyLinkedList:  # A linked list that i've made
    def __init__(self):
        self.head = TextNode()

# My easy traversal to a TextNode which has some text
    def traverse(self, text_to_visit):
        current_node = self.head
        while current_node.val != text_to_visit:
            current_node = current_node.next
        return current_node

# My easy traversal to the last TextNode
    def traverse(self):
        current_node = self.head
        while current_node.next.val is not None:
            current_node = current_node.next
        return current_node

# Add a node to the front
    def add_to_front(self, text):
        new_node = TextNode(text, self.head)
        self.head = new_node

# Add a node to the end
    def add_to_end(self, text):
        last_node = self.traverse()
        new_node = TextNode(text, None)
        last_node.next = new_node


init = MyLinkedList()

print(init.head)

