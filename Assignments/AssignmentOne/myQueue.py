# A queue for project1 of CMPT435.

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"

from myLinkedList import MyLinkedList


class MyQueue(object):
    """A queue generated without the assistance of external libraries for CMPT435.

    A queue generated separate from any pre-existing libraries, for the purpose of learning how to use
    Queues for Allan Labouseur's algorithms class.
    """
    def __init__(self):
        """Initializes MyQueue"""
        self.inner_list = MyLinkedList()

    def enqueue(self, to_enqueue):
        """Adds an item to MyQueue.

        Appends an item to the end of MyQueue.

        Args:
            to_enqueue: The item that is to be appended to MyQueue.

        Returns:
            None
        """
        self.inner_list.add_to_end(to_enqueue)

    def dequeue(self):
        """Removes an item from MyQueue.

        Removes the foremost item from MyQueue and returns it's value.

        Returns:
            The value of the item that was removed from MyQueue.
        """
        removed_val = self.inner_list.remove_from_front()
        return removed_val
