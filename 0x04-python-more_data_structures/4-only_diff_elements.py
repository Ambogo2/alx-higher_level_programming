#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_diff = set()
    for element in set_1:
        if element not in set_2:
            set_diff.add(element)
    for element in set_2:
        if element not in set_1:
            set_diff.add(element)
    return set_diff
