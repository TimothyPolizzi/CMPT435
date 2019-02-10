# A queue for project1 of CMPT435.

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"

from Assignments.AssignmentOne.MyLinkedList import MyLinkedList


class MyQueue(MyLinkedList):
    """A queue generated without the assistance of external libraries for CMPT435.

    A queue generated separate from any pre-existing libraries, for the purpose of learning how to use
    Queues for Allan Labouseur's algorithms class.
    """
    def __init__(self):
        """Initializes MyQueue"""
        super().__init__()
        self.inner_list = MyLinkedList()
        self.inner_list.tail = None

    def enqueue(self, to_enqueue: str):
        """Adds an item to MyQueue.

        Appends an item to the end of MyQueue.

        Args:
            to_enqueue: The item that is to be appended to MyQueue.
        """
        new_node = self.inner_list.TextNode(to_enqueue, None)
        if self.inner_list.is_empty():
            self.inner_list.head = new_node
            self.inner_list.tail = new_node
        else:
            self.inner_list.tail.next = new_node
            self.inner_list.tail = new_node

    def dequeue(self) -> str:
        """Removes an item from MyQueue.

        Removes the foremost item from MyQueue and returns it's value.

        Returns:
            The value of the item that was removed from MyQueue.
        """
        if self.inner_list.is_empty():
            raise Exception('List is empty')
        else:
            old_head_val = self.inner_list.head.val
            self.inner_list.head = self.inner_list.head.next
            return old_head_val
