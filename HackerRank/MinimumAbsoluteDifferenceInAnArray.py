
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         5.2.28
# Site:         HackerRank
# Section:      3 Month Prep - Week 4
# Problem:      Minimum Absolute Difference in an Array

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    
    arr.sort()
    
    abs = 0
    min = 10000000
    i = 0
    j = 0
    
    # length = int(len(arr) / 2)
    length = len(arr)
    
    # print(length)
    
    while i < length:
        
        if(min == 0):
            return 0
        
        j = 0
        while j < length:
            
            if not j == i:
                abs = arr[i] - arr[j]
                
                if(abs < 0):
                    abs *= -1
                
                if abs < min:
                    min = abs
            
            
            j += 1
        
        i += 1
    
    # for el in arr:
    #     for ele in arr:
    #         if ele - el >= 0:
    #             abs = ele - el
    #             if abs < min:
    #                 min = abs
    #         elif ele - el < 0:
    #             abs = (ele - el) * -1
    #             if abs < min:
    #                 min = abs
    
    
    return min

if __name__ == '__main__':

    arr = [-2,2,4]
    arr = [3,-7,0]
    arr = [-59,-36,-13,1,-53,-92,-2,-96,-54,75]

    result = minimumAbsoluteDifference(arr)
    print(result)













