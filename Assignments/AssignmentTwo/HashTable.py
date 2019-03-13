# An implementation of a hash table for CMPT435.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

from typing import List


class HashTable(object):
    """Creates a table with quick insertion and removal using a calculated value.

    Calculates a hash value for every item added to the table. The hash value determines where the item is inserted into
    the list, and allows a large amount of items to be inserted with relative ease into a smaller list. If any insertion
    would cause two items to go into the same place in the list, take the item already in the list and link it to the
    new item.
    """

    class __HashTableItem(object):
        """Creates an item for inside the hash table.

        An item to store things in the hash table.
        """
        def __init__(self, value: str):
            self.val = value
            self.next = None

    def __init__(self):
        self.table_size = 250
        self.internal_table = [None] * self.table_size
        self.size = 0
        self.comparisons = 0

    def insert(self, to_add: str):
        """Adds an item to the hash table.

        Takes the given string to_add and calculates its hash value to add it to the table. If the hash value is already
        taken by another item, sets the previous item to have a pointer to the new item.

        Args:
            to_add(str): The string value that is to be added to the hash table.
        """
        hash_val = self.calculate_hash(to_add)

        if self.internal_table[hash_val] is None:
            self.internal_table[hash_val] = self.__HashTableItem(to_add)
        else:
            current_chain = self.internal_table[hash_val]
            while current_chain.next is not None and current_chain.val is not to_add:
                current_chain = current_chain.next
            current_chain.next = self.__HashTableItem(to_add)

        self.size = self.size + 1

    def remove(self, to_remove: str) -> str:
        """Removes a item from the hash table.

        Removes a given string item from the hash table.

        Args:
            to_remove(str): The item that is to be removed from the hash table.

        Returns:
            The string that is removed from the hash table.
        """
        self.comparisons = 0
        self.comparisons = self.comparisons + 1

        hash_val = self.calculate_hash(to_remove)
        to_return = None

        if self.internal_table[hash_val] is not None:
            previous = None
            current = self.internal_table[hash_val]
            while current.next is not None and current.val is not to_remove:
                self.comparisons = self.comparisons + 1
                previous = current
                current = current.next

            if current.val is to_remove:
                self.comparisons = self.comparisons + 1
                if previous is None:
                    to_return = current
                    self.internal_table[hash_val] = current.next
                else:
                    to_return = current
                    previous.next = current.next

        print(self.comparisons)
        return to_return

    def get_list(self, to_find: int) -> List[str]:
        """Gets the internal list of items at a given hash value.

        Gets the list of items at the hash value specified.

        Args:
            to_find(int): The integer hash value of the position in the hash table that you are trying to find.

        Returns:
            The list of items stored at that hash value.
        """
        current = self.internal_table[to_find]
        return_list = None

        if current is not None:
            return_list = [current.val]

            while current.next is not None:
                current = current.next
                return_list.append(current.val)

        return return_list

    def empty(self):
        """Cleans out the hash table of all values.

        Completely empties the hash table.
        """
        self.internal_table = []

    def calculate_hash(self, to_calculate: str) -> int:
        """Calculate the hash value for a string.

        Calculates the specific hash value for a string in this hash table.

        Args:
            to_calculate(str): The string who's hash value needs to be calculated.

        Returns:
            The integer hash value of to_calculate for this hash table.
        """

        to_calculate = to_calculate.upper()
        letter_total = 0

        # Iterate over all letters in the string, totalling their ASCII values.
        for i in to_calculate:
            this_value = ord(i)
            letter_total = letter_total + this_value

            # Test: print the char and the hash.
            # (if you're using pycharm, command + / can comment out highlighted sections)
            # print(" [")
            # print(i)
            # print(this_value)
            # print("] ")

        # Scale letter_total to fit in table_size.
        hash_code = (letter_total * 1) % self.table_size
        # TODO: Experiment with letterTotal * 2, 3, 5, 50, etc.

        return hash_code
