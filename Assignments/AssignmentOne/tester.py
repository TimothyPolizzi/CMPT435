#!/usr/bin/env python

# A pit of test code for project1 of CMPT435.

__author__ = "Tim Polizzi"
__email__ = "Timothy.Polizzi1@marist.edu"

from myLinkedList import MyLinkedList
from myQueue import MyQueue
from myStack import MyStack
from PalindromeCheck import check_file_for_palindromes

my_list = MyLinkedList()
queue = MyQueue()
stack = MyStack()


def main():
    # test_add_to_front()
    test_add_to_end()
    # test_traverse()
    test_evil()
    # test_remove()
    # test_dequeue()
    # test_pop()
    # test_run('')


def test_run(test_path):
    check_file_for_palindromes(test_path)


def test_add_to_front():
    my_list.add_to_front("one")
    my_list.add_to_front("two")
    my_list.add_to_front("three")

    stack.push("one")
    stack.push("two")
    stack.push("three")


def test_add_to_end():
    my_list.add_to_end("one")
    my_list.add_to_end("two")
    my_list.add_to_end("three")

    queue.enqueue("one")
    queue.enqueue("two")
    queue.enqueue("three")


def test_traverse():
    print(my_list.traverse().val)
    my_list.traverse("two")


def test_remove():
    print(my_list.remove_from_front())
    print(my_list.remove_from_front())
    print(my_list.remove_from_front())
    # print(my_list.remove_from_front())


def test_dequeue():
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    # print(queue.dequeue())


def test_pop():
    print(stack.pop)
    print(stack.pop)
    print(stack.pop)
    # print(stack.pop)


def test_evil():
    print(my_list.evil_traversal("three").val)
    print(my_list.evil_traversal("one").val)
    print(my_list.evil_traversal("four").val)


if __name__ == '__main__':
    main()
