#!/usr/bin/env python

"""euclidean_algorithm_lcm.py: Uses the Euclidean algorithm to obtain the least common multiple"""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"

from euclidean_algorithm_gcd import gcd


def lcm(x, y, verbose=False):
    lcm = (x * y) // gcd(x, y, verbose)
    if verbose:
        print(f"The least common multiple of lcm({x}, {y}) is {lcm}")
    return lcm


if __name__ == "__main__":
    lcm(3524578, 2178309, True)



