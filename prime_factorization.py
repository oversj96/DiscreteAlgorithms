#!/usr/bin/env python

"""prime_factorization.py: Calculate all the prime factors of a number."""

__author__ = "Justin Overstreet"
__copyright__ = "oversj96.github.io"

def prime_factorization(number):
    factors = []
    for i in range(2, number+1):
        while(number % i == 0):
            factors.append(i)
            number /= i
    return factors

if __name__ == "__main__":
    print(prime_factorization(8561400))