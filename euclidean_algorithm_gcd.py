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
            print(f"{'Step ' + str(i+1) + ':':<10} {dividend:>8} = "
                  f"{'(' + str(dividend//divisor) + ')' + '(' + str(divisor) + ')':<10}  +   {remainder}")
        dividend = divisor
        divisor = remainder
        remainder = dividend % divisor
        if remainder is 0 and verbose:
            print(f"{'Too far:':<10} {dividend:>8} = "
                  f"{'(' + str(dividend//divisor) + ')' + '(' + str(divisor) + ')':<12}"
                  f"+   {remainder}")
        i += 1
    if verbose:
        print(f"The gcd({o_dividend}, {o_divisor}) is {str(divisor)}")
    return divisor


if __name__ == "__main__":
    gcd(3123, 1886, True)