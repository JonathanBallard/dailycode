
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.20.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 3
# Problem:      MaximumPerimeterTriangle

#~ -----------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    
    sticks.sort()
    
    a, b, c = sticks[0], sticks[1], sticks[2]
    
    triList = []
    solution = []
    i = 0
    highNum = 0
    highMin = 0
    solList = []
    
    while i < len(sticks):
        a = sticks[i]
        j = 0
        
        while j < len(sticks):
            b = sticks[j]
            k = 0
            
            while k < len(sticks):
                if not k == i and not k == j and not j == i:
                    c = sticks[k]
                    
                    if a + b > c and a + c > b and b + c > a:
                        triList.append([a,b,c])
                
                k += 1
            j += 1
        i += 3
    
    
    triList = sorted(triList, reverse = True)
    for tri in triList:
        if(tri[0] + tri[1] + tri[2] > highNum):
            highNum = tri[0] + tri[1] + tri[2]
            
            solList.append(tri)
    
    
    for tri in solList:
        tri.sort()
        if(tri[0] > highMin):
            highMin = tri[0]
            solution = tri
    
    
    if solution == []:
        return [-1]
    else:
        return solution
    

if __name__ == '__main__':


    sticks = [1,2,3,4,5,10]
    sticks2 = [1,1,1,3,3]
    sticks3 = [1,2,3]

    result = maximumPerimeterTriangle(sticks3)

    print(result)






















