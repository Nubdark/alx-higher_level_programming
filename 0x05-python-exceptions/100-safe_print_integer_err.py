#!/usr/bin/python3
import sys


def safe_print_integer_err(val):
    try:
        print("{:d}".format(val))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
