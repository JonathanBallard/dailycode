
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.25.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 4
# Problem:      Left Rotation

#~ -----------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    i = 0
    n = len(arr)
    retArr = []
    
    while i < n:
        retArr.append(arr[((i + d) % n)])
        i += 1
    
    return retArr

if __name__ == '__main__':

    d = 2

    arr = [1,2,3,4,5]

    result = rotateLeft(d, arr)

    print(result)






















