# A stack for project1 of CMPT435.

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"

from myLinkedList import MyLinkedList


class MyStack(object):
    """A stack generated without the assistance of external libraries for CMPT435.

    A stack generated separate from any pre-existing libraries, for the purpose of learning how to
    use stacks for Allan Labouseur's algorithms class.
    """
    def __init__(self):
        """Initializes MyStack"""
        self.inner_list = MyLinkedList()

    def push(self, to_push):
        """Adds an item to MyStack.

        Appends an item to the top of MyStack.

        Args:
            to_push: The item that is to be appended to MyStack.
        """
        self.inner_list.add_to_front(to_push)

    def pop(self):
        """Removes an item from MyStack.

        Removes the topmost item from MyStack and returns its value.

        Returns:
            The value of the item that was removed from MyStack.
        """
        popped_node = self.inner_list.remove_from_front()
        return popped_node

    def peek(self):
        """Returns the value of the item on top of MyStack."""
        peek_val = self.pop
        self.push(peek_val)
        return peek_val
