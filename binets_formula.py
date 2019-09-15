#!/usr/bin/env python

"""binets_formula.py: Instantly determine the nth number in the fibonacci or lucas sequences."""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"

import numpy as np
from decimal import Decimal


def nth_fib(n):
    root_five = np.sqrt(5)
    return Decimal((1 / root_five) * ((((1 + root_five) / 2) ** n) - (((1 - root_five) / 2) ** n)) ** n)


def nth_lucas(n):
    root_five = np.sqrt(5)
    return round(((1 + root_five) / 2) ** n - ((1 - root_five) / 2) ** n)


if __name__ == "__main__":
    print(nth_fib(65))
    print(nth_fib(78))
    print(nth_fib(87))
    print(nth_lucas(65))
    print(nth_lucas(78))