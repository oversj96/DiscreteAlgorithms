#!/usr/bin/env python

"""euclidean_algorithm_lcm.py: Uses the Euclidean algorithm to obtain the least common multiple"""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"

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
        while i > 0:
            substring = f"(substitute {str(remainders[i-1])}=(1)({str(dividends[i-1])}) - ({str(quotients[i-1])})({str(divisors[i-1])})"
            print(f"{remainders[i]}=(1)({dividends[i]}) - ({quotients[i]})({remainders[i-1]}) {substring}")
            i -= 1
    print()

gcd_linear_combo((3524578, 2178309)