#!/usr/bin/env python

"""binets_formula.py: Instantly determine the nth number in the fibonacci or lucas sequences."""

__author__ = "Justin Overstreet"
__copyright__ = "oversj96.github.io"

import numpy as np


def nth_fib(n):
    golden = (1 + 5 ** 0.5) / 2
    return int(np.round(np.power(golden, n) / np.sqrt(5)))


def nth_lucas(n):
    golden = (1 + 5 ** 0.5) / 2
    return int(round(np.power(golden, n)))


if __name__ == "__main__":
    print(nth_fib(65))
    print(nth_fib(78))
    print(nth_fib(87))
    print(nth_lucas(65))
    print(nth_lucas(78))