
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.24.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 4
# Problem:      Picking Numbers

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    
    nums = [0] * 100
    i = 0
    while i < len(a):
        nums[a[i]] += 1
        i += 1
    
    
    maxTot = 0
    currTot = 0
    k = 1
    while k < len(nums) - 1:
        currTotA = nums[k - 1] + nums[k]
        currTotB = nums[k] + nums[k + 1]
        currTot = currTotA
        
        if(currTotB > currTotA):
            currTot = currTotB
        
        if(currTot > maxTot):
            maxTot = currTot
        
        k += 1

    return maxTot


if __name__ == '__main__':


    a = [1,1,2,2,4,4,5,5,5]
    a2 = [4, 6, 5, 3, 3, 1]
    a3 = [66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66]
    a4 = [98, 3, 99, 1, 97, 2]
    a5 = [4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1, 99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4]
    a6 = [7, 12, 13, 19, 17, 7, 3, 18, 9, 18, 13, 12, 3, 13, 7, 9, 18, 9, 18, 9, 13, 18, 13, 13, 18, 18, 17, 17, 13, 3, 12, 13, 19, 17, 19, 12, 18, 13, 7, 3, 3, 12, 7, 13, 7, 3, 17, 9, 13, 13, 13, 12, 18, 18, 9, 7, 19, 17, 13, 18, 19, 9, 18, 18, 18, 19, 17, 7, 12, 3, 13, 19, 12, 3, 9, 17, 13, 19, 12, 18, 13, 18, 18, 18, 17, 13, 3, 18, 19, 7, 12, 9, 18, 3, 13, 13, 9, 7]

    result = pickingNumbers(a6)
    print(result)
    # print(len(a3))

















