#!/usr/bin/env python

"""knapsack_problem.py: Determine maximum weight you can carry given the combinations"""

__author__ = "Justin Overstreet"
__copyright__ = "oversj86.github.io"
# [14, 16, 21, 25, 32]
def knapsack_problem(combos, max_weight):
    bits = [False for i in range(0, len(combos))]
    combos = 2**len(bits)
    for combo in range(0, combos):
        
