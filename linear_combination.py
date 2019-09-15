#!/usr/bin/env python

"""euclidean_algorithm_lcm.py: Uses the Euclidean algorithm to obtain the least common multiple"""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"

import sympy

def gcd_linear_combo(dividend, divisor):
    remainder = dividend % divisor
    o_dividend = dividend
    o_divisor = divisor
    divisors = [divisor]
    dividends = [dividend]
    remainders = [remainder]
    quotients = [dividend//divisor]
    i = 0
    while remainder > 0:
        dividend = divisor
        divisor = remainder
        remainder = dividend % divisor
        if remainder is not 0:
            dividends.append(dividend)
            divisors.append(divisor)
            remainders.append(remainder)
            quotients.append(dividend//divisor)
        i += 1
    sub_state = 'right'
    for step in range(len(remainders) - 1, -1, -1):
        if sub_state is 'right':
        



gcd_linear_combo(3524578, 2178309)