# A stack for project1 of CMPT435. Also for fun.

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"


class ArrayStack(object):
    """A stack object generated using an array.

    A fun little project creating a stack using an array for better space usage.
    """
    def __init__(self):
        """Initializes ArrayStack"""
        self.inner_list = []
        self.top = -1

    def push(self, to_push):
        """Adds an item to ArrayStack.

        Appends an item to the top of ArrayStack.

        Args:
            to_push: The value of the item that is to be pushed to the top of ArrayStack
        """
        self.inner_list[self.top] = to_push
        self.top = self.top + 1

    def pop(self):
        """Removes an item from ArrayStack

        Removes the item at top from ArrayStack

        Returns:
            The value of the item removed from ArrayStack
        """
        to_return = self.inner_list[self.top]
        self.inner_list[self.top] = None
        self.top = self.top - 1
        return to_return

    def is_empty(self):
        """Returns True if the Stack is empty, False otherwise."""
        to_return = False
        if self.top is -1:
            to_return = True
        return to_return

    def peek(self):
        """Returns the topmost value of arrayStack."""
        return self.inner_list[self.top]
