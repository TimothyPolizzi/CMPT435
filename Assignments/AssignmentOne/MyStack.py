# A stack for project1 of CMPT435.

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"

from Assignments.AssignmentOne.MyLinkedList import MyLinkedList


class MyStack(MyLinkedList):
    """A stack generated without the assistance of external libraries for CMPT435.

    A stack generated separate from any pre-existing libraries, for the purpose of learning how to
    use stacks for Allan Labouseur's algorithms class.
    """

    def __init__(self):
        """Initializes MyStack"""
        super().__init__()
        self.inner_list = MyLinkedList()

    def push(self, to_push: str):
        """Adds an item to MyStack.

        Appends an item to the top of MyStack.

        Args:
            to_push: The item that is to be appended to MyStack.
        """
        new_node = self.inner_list.TextNode(to_push, self.inner_list.head)
        self.inner_list.head = new_node

    def pop(self) -> str:
        """Removes an item from MyStack.

        Removes the topmost item from MyStack and returns its value.

        Returns:
            The value of the item that was removed from MyStack.
        """
        if self.inner_list.is_empty():
            raise Exception('List is empty')
        else:
            old_head_val = self.inner_list.head.val
            self.inner_list.head = self.inner_list.head.next
            return old_head_val

    def peek(self) -> str:
        """Returns the value of the item on top of MyStack."""
        peek_val = self.pop
        self.push(str(peek_val))
        return str(peek_val)
