#!/usr/bin/python3
"""This module defines class mylist"""


class MyList(list):
    """MyList; class that defines MyList"""

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        sorted_list= sorted(self)
        print(sorted_list)
