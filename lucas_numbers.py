#!/usr/bin/env python

"""lucas_numbers.py: Generate a sequence of lucas numbers up to the nth term"""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"


def lucas_numbers(signature, n):
    n += 1
    for i in range(0, n - len(signature)):
        signature.append(sum(signature[-2:]))
    return signature[n - 1], signature[:n]


if __name__ == "__main__":
    print(lucas_numbers([2, 1], 78))

