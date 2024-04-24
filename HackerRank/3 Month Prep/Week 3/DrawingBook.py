
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.22.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 3
# Problem:      Drawing Book

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    
    mid = int(n / 2)
    
    numFront = 0
    numBack = 0
    
    if(n % 2 == 0):
        n += 1

    if(p <= mid):
        i = 1
        while i < n:
            if(i == p or i - 1 == p):
                return numFront
            else:
                numFront += 1
                i += 2
    elif(p > mid):
        i = n
        while i > 0:
            if(i == p or i - 1 == p):
                return numBack
            else:
                numBack += 1
            i -= 2


if __name__ == '__main__':


    p = 5   # page to turn to

    n = 6   #total number of pages (last page will ALWAYS be odd)
    
    result = pageCount(n, p)
    
    print(result)


# 1,23,45
# 1,23,45,67,89,1011













