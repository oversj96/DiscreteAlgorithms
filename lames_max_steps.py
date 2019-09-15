#!/usr/bin/env python

"""lames_max_steps.py: Determine the maximum number of steps needed to compute the gcd of two numbers using the
euclidean algorithm."""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"

import mpmath


def gcd_max_steps(divisor):
    # mpmath.phi represents the golden ratio.
    return mpmath.log(divisor, mpmath.phi) + 1


if __name__ == "__main__":
    print(gcd_max_steps(2178309))