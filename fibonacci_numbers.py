#!/usr/bin/env python

"""fibonacci_numbers.py: Generate a sequence of fibonacci numbers up to the nth term"""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"


def fibonacci_numbers(signature, n):
    n += 1
    for i in range(0, n - len(signature)):
        signature.append(sum(signature[-2:]))
    return signature[n-1], signature[:n]


if __name__ == "__main__":
    print(fibonacci_numbers([0, 1], 78))