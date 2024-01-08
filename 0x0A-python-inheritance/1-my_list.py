#!/usr/bin/python3
"""A module for class mylist"""

class MyList(list):
    """MyList:defines mylist class"""

    def print_sorted(self):
        """
        print_sorted:prints list in sorted assending order.
        """
        sorted_list= sorted(self)
        print(sorted_list)



