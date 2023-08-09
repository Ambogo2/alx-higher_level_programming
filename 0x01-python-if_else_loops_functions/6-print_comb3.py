#!/usr/bin/python3
for i in range(0, 10):
    for digits in range(i + 1, 10):
        if i == 8 and digits == 9:
            print("{}{}".format(i, digits))
        else:
            print("{}{}, ".format(i, digits), end="")
