# A linked list written for the intention of making it into a stack or queue

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"


class MyLinkedList:
    """A linked list generated without the assistance of external libraries for CMPT435.

    A linked list generated separate from any pre-existing libraries, for the purpose of learning how to use
    linked lists for Allan Labouseur's algorithms class.
    """
    def __init__(self):
        """Initializes MyLinkedList"""
        self.head = None

    class TextNode(object):
        """A node containing text used for MyLinkedList.

        A node used to create MyLinkedList that can contain text values.
        """

        def __init__(self, *foo):
            """Initializes TextNode.

            Will create an instance of TextNode that either will have no set values, or a preset
            value and pointer to another TextNode.

            Args:
                *foo: The commands list which can either contain two or no arguments.
                *foo[0](String): The text value which the TextNode will contain.
                *foo[1](TextNode): The pointer to the next TextNode in MyLinkedList.
            """
            if len(foo) == 0:  # Constructor for an empty call of TextNode
                self.val = ""
                self.next = ""
            elif len(foo) == 2:  # Constructor for TextNode with predefined text and next node
                internal_text = foo[0]
                next_node = foo[1]
                self.val = internal_text
                self.next = next_node
            else:
                raise Exception('TextNode must be initialized with either two or no arguments.')

    def traverse(self, *foo):
        """Traverse MyLinkedList either to a specified TextNode or to the last TextNode.

        Will transverse MyLinkedList to the last node if no value is given as a parameter, or will
        traverse to the first TextNode with the vale of the parameter given.

        Args:
            *foo: The commands list which can either contain one or no arguments.
            *foo[0](String): The string value of the text node that is to be traversed to.

        Returns:
            The TextNode that was traversed to.
        """
        if not self.is_empty():
            current_node = self.head

            if len(foo) == 1:  # Traversal to find a particular TextNode
                text_to_visit = foo[0]
                while current_node.val is not text_to_visit:
                    current_node = current_node.next
            elif len(foo) == 0:  # Traversal to find the last node in the list
                    while current_node.next is not None:
                        current_node = current_node.next
        else:
            current_node = None

        return current_node

    def is_empty(self):
        """Returns True if MyLinkedList contains no TextNodes, False otherwise"""
        to_return = False
        if self.head is None:
            to_return = True
        return to_return

    def add_to_front(self, text):
        """Appends a TextNode to the front of MyLinkedList

        Args:
            text(String): The value of the TextNode that is to be appended to MyLinkedList
        """
        new_node = self.TextNode(text, self.head)
        self.head = new_node

    def add_to_end(self, text):
        """Appends a TextNode to the end of MyLinkedList

        Args:
            text(String): The value of the TextNode that is to be appended to MyLinkedList
        """
        new_node = self.TextNode(text, None)
        if self.is_empty():
            self.head = new_node
        else:
            last_node = self.traverse()
            last_node.next = new_node

    def remove_from_front(self):
        """Removes the first node from MyLinkedList

        Returns:
            The value of the node that is removed from MyLinkedList
        """
        if self.is_empty():
            raise Exception('List is empty')
        else:
            old_head_val = self.head.val
            self.head = self.head.next
            return old_head_val
