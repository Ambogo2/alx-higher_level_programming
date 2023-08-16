#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_common = set()
    for elements in set_1:
        if elements in set_2:
            set_common.add(elements)
    return set_common
