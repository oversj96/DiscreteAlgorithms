#!/usr/bin/env python

"""fermat_factorization.py: Factor an odd natural number"""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"

import math as m


def fermat_factorization(number, verbose=False):
    if number % 2 is 0 or type(number) is not int or number < 1:
        print(f"The number entered was invalid. Input must be an odd natural number.")
        return None
    else:
        n = m.ceil(m.sqrt(number))
        if verbose:
            print(f"The square root of {number} is approximately {m.sqrt(number):.5f}, so we choose"
                  f" {n} for our n. \n")
        square = (n ** 2) - number
        while not perfect_square(square):
            if verbose:
                print(f"({n})^2 - {number} = {square} (is not a perfect square)")
            n += 1
            square = (n**2) - number
        root = int(m.sqrt(square))
        if verbose:
            print(f"({n})^2 - {number} = {square} (is a perfect square: {square} = ({root})^2)\n")
            print(f"{number} = ({n})^2 - ({root})^2 = ({n} + {root})({n} - {root}) = ({n + root})"
                  f"({n - root})")
        return n + root, n - root


def perfect_square(n):
    check = m.sqrt(n)
    return (check - m.floor(check)) == 0


if __name__ == "__main__":
    print(fermat_factorization(5429, True))
