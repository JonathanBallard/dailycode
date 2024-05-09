
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         5.8.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 5
# Problem:      Max Min

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    
    arr.sort()
    
    i = 0
    subArr = arr[:k]
    minComp = subArr[len(subArr) - 1] - subArr[0]
    
    while i < len(arr):
        subArr = arr[i:k + i]
        subArr.sort()
        min = subArr[len(subArr) - 1] - subArr[0]
        
        if(min < minComp and len(subArr) == k):
            minComp = min
        
        # subArr2 = arr[len(arr) - k - i:len(arr) - 1 ]
        # subArr2.sort()
        
        # min = subArr2[len(subArr2) - 1] - subArr2[0]
        
        # if(min < minComp and len(subArr2) == k):
        #     minComp = min
        
        
        i += 1
    
    return minComp

if __name__ == '__main__':

    k = 2
    arr = [1,4,7,2]
    

    k0 = 4
    arr0 = [1,2,3,4,10,20,30,40,100,200]
    
    k2 = 5
    arr2 = [4504,1520,5857,4094,4157,3902,822,6643,2422,7288,8245,9948,2822,1784,7802,3142,9739,5629,5413,7232]
    
    k3 = 8
    arr3 = [6327,571,6599,479,7897,9322,4518,571,6677,7432,815,6920,4329,4104,7775,5708,7991,5802,8619,6053,7539,7454,9000,3267,6343,7165,4095,439,5621,4095,153,1948,1018,6752,8779,5267,2426,9649,2190,9103,7081,3006,2376,7762,3462,151,3471,1453,2305,8442]
    
    k4 = 2
    arr4 = []
    
    
    
    # result0 = maxMin(k0, arr0)
    # print(result0)
    
    # result3 = maxMin(k3, arr3)
    # print(result3)
    
    result = maxMin(k, arr)
    print(result)


















