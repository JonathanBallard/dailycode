
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.26.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 4
# Problem:      Number Line Jumps

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    i = 0
    while i <= 10000:
        if(x1 + (v1 * i) == x2 + (v2 * i)):
            return 'YES'
        i += 1
    
    return 'NO'

if __name__ == '__main__':

    x1 = 10
    v1 = 1

    x2 = 0
    v2 = 5

    result = kangaroo(x1, v1, x2, v2)

    print(result)














