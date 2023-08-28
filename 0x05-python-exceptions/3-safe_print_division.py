#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except TypeError:
        div = none
    except ZeroDivisionError:
        div = none
    finally:
        print("Inside result:{}".format(div))
    return div
