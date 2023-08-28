#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for integers in range(x):
        try:
            print("{:d}".format(my_list, end=""))
            count += 1
        except Exception:
            continue
    print("")
    return count