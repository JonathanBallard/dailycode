
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.14.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 2
# Problem:      Flipping Bits

#~ -----------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    
    # Bitwise NOT (flip bits) bitwise AND ((2^32) - 1) to ensure positives (since working with unsigned long)
    return ~n & 2 ** 32 - 1

if __name__ == '__main__':
    
    length = 3
    n = [2147483647, 1, 0 ]

    for el in n:
        result = flippingBits(el)
        print(result)




















