# A queue for project1 of CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from Assignments.AssignmentOne.MyLinkedList import MyLinkedList


class MyQueue(MyLinkedList):
    """A queue generated without the assistance of external libraries for CMPT435.

    A queue generated separate from any pre-existing libraries, for the purpose of learning how to use
    Queues for Alan Labouseur's algorithms class.
    """

    def __init__(self):
        """Initializes MyQueue"""
        super().__init__()
        self.tail = None

    def enqueue(self, to_enqueue: str):
        """Adds an item to MyQueue.

        Appends an item to the end of MyQueue.

        Args:
            to_enqueue: The item that is to be appended to MyQueue.
        """
        new_node = self.TextNode(to_enqueue, None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self) -> str:
        """Removes an item from MyQueue.

        Removes the foremost item from MyQueue and returns it's value.

        Returns:
            The value of the item that was removed from MyQueue.
        """
        if self.is_empty():
            raise Exception('List is empty')
        else:
            old_head_val = self.head.val
            self.head = self.head.next
            return old_head_val
