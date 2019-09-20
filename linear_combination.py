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
    i = -1
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
    left_factor = dividends[i]
    left_multiplier = quotients[i]
    right_factor = divisors[i]
    right_multiplier = 1
    remainder = remainders[i]
    print(f"{remainder} = ({left_multiplier})({left_factor}) - ({right_multiplier})({right_factor})")
    while i is not 0:
        if right_factor is remainders[i-1]:
            next_left_mult = 1
            next_right_mult = quotients[i-1]
            next_left_factor = dividends[i-1]
            next_right_factor = divisors[i-1]
            print(f"{remainder} = ({left_multiplier})({left_factor}) - ({right_multiplier})({right_factor})"
                  f" (substitute {right_factor}=({next_left_mult})({next_left_factor}) - "
                  f"({next_right_mult})({next_right_factor}))")
            print(f"{remainder} = ({left_multiplier})({left_factor}) - ({right_multiplier})"
                  f"[({next_left_mult})({next_left_factor}) - ({next_right_mult})({next_right_factor})]")
            next_right_mult *= right_multiplier
            next_left_mult *= right_multiplier
            print(f"{remainder} = ({left_multiplier})({left_factor}) - ({next_left_mult})({next_left_factor})"
                  f" + ({next_right_mult})({next_right_factor})")
            left_multiplier += next_right_mult
            right_multiplier = next_left_mult
            right_factor = next_left_factor
            print(f"{remainder} = ({left_multiplier})({left_factor}) - ({right_multiplier})({right_factor})")
        elif left_factor is remainders[i-1]:
            next_left_mult = 1
            next_right_mult = quotients[i-1]
            next_left_factor = dividends[i-1]
            next_right_factor = divisors[i-1]
            print(f"{remainder} = ({left_multiplier})({left_factor}) - ({right_multiplier})({right_factor})"
                  f" (substitute {left_factor}=({next_left_mult})({next_left_factor}) - "
                  f"({next_right_mult})({next_right_factor}))")
            print(f"{remainder} = ({left_multiplier})[({next_left_mult})({next_left_factor}) - "
                  f"({next_right_mult})({next_right_factor})]"
                  f" - ({right_multiplier})({right_factor})")
            next_right_mult *= left_multiplier
            next_left_mult *= left_multiplier
            print(f"{remainder} = ({next_left_mult})({next_left_factor}) - {next_right_mult}({next_right_factor})"
                  f" - ({right_multiplier})({right_factor})")
            right_multiplier += next_right_mult
            left_factor = next_left_factor
            print(f"{remainder} = ({left_multiplier})({left_factor}) - ({right_multiplier})({right_factor})")
        i -= 1



if __name__ == "__main__":
    gcd_linear_combo(336, 60)