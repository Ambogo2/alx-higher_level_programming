#!/usr/bin/python3
import sys  # Import the sys module to access stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False
