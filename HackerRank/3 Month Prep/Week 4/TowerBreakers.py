
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         5.2.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 4
# Problem:      Tower Breakers

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    
    if(n % 2 == 0 or m == 1):
        return 2
    else:
        return 1
        
    

if __name__ == '__main__':



    n = 1

    m = 4

    result = towerBreakers(n, m)

    print(result)
















