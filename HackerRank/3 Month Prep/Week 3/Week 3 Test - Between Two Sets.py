
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.24.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 3
# Problem:      Week 3 Mock Test - Between Two Sets

#~ -----------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    
    a.sort()
    b.sort()
    
    result = 0
    intCheck = a[len(a) - 1]
    k = 0
    j = 1
    aList = []
    finalList = []
    
    # Check array 'a'
    while intCheck < b[0]:
        i = 0
        isFactor = True
        while (i < len(a) and isFactor == True):
            
            if not (intCheck % a[i] == 0):
                isFactor = False
            i += 1
        
        if(isFactor == True):
            aList.append(intCheck)
            
        intCheck += 1

    # print('aList: ' + str(aList))
    

    
    while k < len(aList):
        j = 0
        isFactor = True
        while j < len(b) and isFactor == True:
            if not (b[j] % aList[k] == 0):
                isFactor = False
                print(b[j])
                print(aList[k])
            j += 1
        
        if(isFactor == True):
            # print('-- ' + str(aList[k]))
            finalList.append(aList[k])
        k += 1
    
    result = len(finalList)
    # print(finalList)
    
    return result

if __name__ == '__main__':

    # first_multiple_input = input().rstrip().split()
    arr = [2, 4]
    n = len(arr)
    

    brr = [16, 32, 96]
    m = len(brr)

    total = getTotalX(arr, brr)

    print(total)















