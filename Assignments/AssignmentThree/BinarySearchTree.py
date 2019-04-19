# A binary search tree for Alan's CMPT435 class.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List


class BinarySearchTree(object):
    class __TreeNode(object):
        def __init__(self, val: str):
            self.value = val
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.size = 0
        self.comparisons = 0
        self.comp_total = 0

    def contains(self, element: str) -> bool:
        """ Checks if a given item exists in the BST.

        Args:
            element: The string value of the item that is being searched for in the BST.

        Returns:
            A boolean true or false, where true is if the item is in the BST and false otherwise.
        """
        self.comparisons = 0

        ret_bool = self.__contains(self.root, element)

        print(self.comparisons)
        self.comp_total += self.comparisons

        return ret_bool

    def __contains(self, node: __TreeNode, element: str) -> bool:
        self.comparisons += 1

        if node is None:
            return False
        elif node.value is element:
            return True

        self.comparisons += 1

        if node.value > element:
            return self.__contains(node.left, element)
        return self.__contains(node.right, element)

    def add(self, element: str) -> __TreeNode:
        """ Adds a new element to the tree in the correct position.

        Appends a new item to the tree in the correct location, where if there are no previous items in the tree makes
        the new item the head, and if there are other items already in the tree appends the item down the correct path.

        Args:
            element (str): The string of what node is being attempted to be added to the tree.

        Returns:
            The value to which the pointer previously pointing to node should point.
        """
        if self.root is None:
            self.root = self.__TreeNode(element)
        else:
            self.root = self.__add(element, self.root)
        self.size += 1
        return self.root

    def __add(self, element: str, node: __TreeNode) -> __TreeNode:
        """ The secret add helper method.

        Recursively moves down the tree attempting to find the end of the branch where the new node will land.

        Args:
            element (str): The string of what node is being attempted to be added to the tree.
            node (__TreeNode): The node which is being traversed on.

        Returns:
            The value to which the pointer previously pointing to node should point.
        """
        if node is None:
            return self.__TreeNode(element)

        if node.value <= element:
            node.right = self.__add(element, node.right)
        else:
            node.left = self.__add(element, node.left)

        return node

    def remove(self, element: str) -> bool:
        """ Removes the specified element from the tree, if the element is in the tree.

        Args:
            element (str): The string value of the element to be removed.

        Returns:
            A boolean true if the element was found and removed, or false otherwise.
        """
        if self.contains(element):
            self.size -= 1
            self.root = self.__remove(self.root, element)
            to_return = True
        else:
            to_return = False

        return to_return

    def __remove(self, node: __TreeNode, element: str) -> __TreeNode:
        if node is None:
            return None

        if node.value > element:
            node.left = self.__remove(node.left, element)

        if node.value < element:
            node.right = self.__remove(node.right, element)

        if node.value is element:
            if node.right is not None and node.left is not None:
                rem = node.right
                while rem.left is not None:
                    rem = rem.left

                swap = node.value
                node.value = rem.value
                rem.value = swap

                node.right = self.__remove(node.right, element)
                return node

            elif node.right is not None:
                return node.right
            elif node.left is not None:
                return node.left
            else:
                return None
        return node

    def depth_first_traversal(self) -> List[str]:
        """ Traverses the BST in a vertical level pattern.

        Returns:
            A list containing the path taken by the traversal.
        """
        new_list = []
        self.__depth_first_traversal(self.root, new_list)
        return new_list

    def __depth_first_traversal(self, node: __TreeNode, ret_list: List[str]):
        if node is None:
            return

        ret_list.append(node.value)
        self.__depth_first_traversal(node.left, ret_list)
        self.__depth_first_traversal(node.right, ret_list)

    def breadth_first_traversal(self) -> List[str]:
        """ Traverses the BST in a horizontal level pattern.

        Returns:
            A list containing the path taken by the traversal.
        """
        return self.__breadth_first_traversal(False)

    def __breadth_first_traversal(self, include_null: bool) -> List[str]:
        ret_list = []
        queue = [self.root]

        while queue:
            head = queue.pop()
            if head is None and include_null:
                ret_list.append(None)
            if head is not None:
                ret_list.append(head.value)
                queue.append(head.left)
                queue.append(head.right)
        return ret_list

    def min(self) -> str:
        """ Returns the smallest value in the BST.

        Returns:
            The smallest value in the BST.
        """
        return self.__min(self.root).value

    def __min(self, node: __TreeNode) -> __TreeNode:
        if node is None:
            return None
        return node.right

    def max(self) -> str:
        """ Returns the largest value in the BST.

        Returns:
            The largest value in the BST.
        """
        return self.__max(self.root).value

    def __max(self, node: __TreeNode) -> __TreeNode:
        if node is None:
            return None
        return node.left

    def __rotate_right(self, node: __TreeNode) -> __TreeNode:
        """ Rotates the BST right around a given point

        Args:
            node (__TreeNode): The node which the tree will be rotated around

        Returns:
            The new root of the BST
        """
        new_root = node.left
        r_to_l = new_root.right

        new_root.right = node
        node.left = r_to_l
        return new_root

    def __rotate_left(self, node: __TreeNode) -> __TreeNode:
        """ Rotates the BST left around a given point

        Args:
            node (__TreeNode): The node which the tree will be rotated around

        Returns:
            The new root of the BST
        """
        new_root = node.right
        r_to_l = new_root.left

        new_root.left = node
        node.right = r_to_l
        return new_root

    def __rotate_right_left(self, node: __TreeNode) -> __TreeNode:
        """ Rotates the BST right then left.

        Args:
            node (__TreeNode): The point around which the BST will be rotating.

        Returns:
            The new root node.
        """
        node.right = self.__rotate_right(node.right)
        node = self.__rotate_left(node)
        return node

    def __rotate_left_right(self, node: __TreeNode) -> __TreeNode:
        """ Rotates the BST left then right.

        Args:
            node (__TreeNode): The point around which the BST will be rotating.

        Returns:
            The new root node.
        """
        node.left = self.__rotate_left(node.left)
        node = self.__rotate_right(node)
        return node
