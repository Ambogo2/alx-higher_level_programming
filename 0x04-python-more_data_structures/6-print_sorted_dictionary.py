#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_sorted = list(a_dictionary.keys())
    keys_sorted.sort()
    for key in keys_sorted:
        print("{}: {}".format(key, a_dictionary.get(key)))
