#!/usr/bin/env python

"""euclidean_algorithm_gcd.py: Uses the Euclidean algorithm to obtain the greatest common denominator"""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"


def gcd(dividend, divisor, verbose=False):
    remainder = dividend % divisor
    o_dividend = dividend
    o_divisor = divisor
    i = 0
    while remainder > 0:
        if verbose:
            print(f"Step {i+1}: {dividend} = ({dividend//divisor})({divisor})   +   {remainder}")
        dividend = divisor
        divisor = remainder
        remainder = dividend % divisor
        if remainder is 0 and verbose:
            print(f"{'Too far'}: {dividend} = ({dividend//divisor})({divisor})   +   {remainder}")
        i += 1
    if verbose:
        print(f"The gcd({o_dividend}, {o_divisor}) is {str(divisor)}")
    return divisor

#  gcd(691, 103)