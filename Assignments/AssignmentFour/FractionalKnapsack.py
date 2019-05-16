# It's for storing a oddly specific amount of a strange spice that some people get REALLY high on.

__author__ = 'Tim Polizzi'
__email__ = 'Timothy.Polizzi1@marist.edu'

# from Assignments.AssignmentFour.Melange import Melange
from Melange import Melange


class FractionalKnapsack(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.total_value = 0
        self.filled_with = []
        self.spice_list = []

    def add_spice(self, spice: Melange):
        """Adds a new spice variant to the list of spices that can be used

        Args:
            spice: The spice to be added to the list of spice variants
        """
        spice_copy = Melange(spice.name, spice.price, spice.qty)
        self.spice_list.append(spice_copy)

    def fill_bag(self):
        """Fills the knapsack with spice to its maximum size for the most possible value

        Returns:
            The list of spices added to the bag
        """

        while self.capacity > 0 and self.spice_left():
            good_spice = self.spice_list[0]

            for spice in self.spice_list:
                if good_spice.qty <= 0:
                    good_spice = spice
                elif spice.price > good_spice.price and spice.qty > 0:
                    good_spice = spice

            spice_to_remove = good_spice.qty

            if spice_to_remove > self.capacity:
                spice_to_remove = self.capacity
            elif spice_to_remove > good_spice.qty:
                spice_to_remove = good_spice.qty

            self.capacity = self.capacity - spice_to_remove
            good_spice.qty = good_spice.qty - spice_to_remove

            self.filled_with.append(good_spice)
            self.total_value = self.total_value + (good_spice.price * spice_to_remove)

        return self.filled_with

    def spice_left(self):
        """Checks to see if there is anymore spice left

        Returns:
            A boolean indicating if there is spice left
        """
        spice_left = False

        for spice in self.spice_list:
            if spice.qty > 0:
                spice_left = True

        return spice_left
