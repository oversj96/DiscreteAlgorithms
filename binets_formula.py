#!/usr/bin/env python

"""binets_formula.py: Instantly determine the nth number in the fibonacci or lucas sequences."""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"

from decimal import Decimal, localcontext
import numpy as np
import mpmath

def nth_fib(n):
    # with localcontext() as ctx:
    #     ctx = 5
    # root_five = Decimal(np.sqrt(5))
    # root_five = np.sqrt(5)
    # return round((1 / root_five) * ((((1 + root_five) / 2) ** n) - (((1 - root_five) / 2) ** n)))
    golden = (1 + 5 ** 0.5) / 2
    return int(np.round(np.power(golden, n) / np.sqrt(5)))

def nth_lucas(n):
    # root_five = np.sqrt(5)
    # return round(((1 + root_five) / 2) ** n - ((1 - root_five) / 2) ** n)
    return int(round(mpmath.power(mpmath.phi, n)))


if __name__ == "__main__":
    print(nth_fib(65))
    print(nth_fib(78))
    print(nth_fib(87))
    print(nth_lucas(65))
    print(nth_lucas(78))