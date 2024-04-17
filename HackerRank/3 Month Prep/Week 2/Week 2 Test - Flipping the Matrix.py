
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.16.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 2
# Problem:      Week 2 Mock Test - Flipping the Matrix

#~ -----------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

# sum of i'th array's first n elements compared with sum of i'th array's last n elements
# if lastN > firstN: Reverse Row
# sum i'th element of first n arrays and compare with sum of i'th element of last n arrays
# if lastN > firstN: Reverse Column



# X-axis
def flipRow(matrix):
    
    print('newMat flipRow start: ' + str(matrix))
    
    newMat = []
    n = math.floor(len(matrix) / 2)
    k = len(matrix) - 1
    
    for arr in matrix:
        sumL = 0
        sumR = 0
        j = 0
        k = len(matrix) - 1
        
        while j < n:
            sumL += arr[j]
            sumR += arr[k]

            j += 1
            k -= j
        
        if(sumR > sumL):
            qArr = arr[::-1]
            newMat.append(qArr)        
            # print('row flip: arr=' + str(arr) + ', newMat: ' + str(newMat))
        else:
            newMat.append(arr)
    
    print('newMat flipRow end: ' + str(matrix))
    return newMat

def flipCol(newMat):
    
    print('newMat flipCol start: ' + str(newMat))
    
    n = math.floor(len(newMat) / 2)
    sumT = 0
    sumB = 0
    l = 0
    q = len(newMat) - 1
    i = 0
    
    returnMat = []
    
    while i < len(newMat):
        while l < n:
            sumT += newMat[l][i]
            sumB += newMat[q][i]
            
            l += 1
            q -= l
        
        subArr = []
        if(sumB > sumT):
            p = 0
            t = len(newMat) - 1
            
            while p < n:
                temp = newMat[p][i]
                
                newMat[p][i] = newMat[t][i]
                newMat[t][i] = temp
                
                if not newMat[p][:i] == []:
                    subArr = newMat[p][:i] + [newMat[t][i]] + newMat[p][i + 1:]
                else:
                    subArr = [newMat[t][i]] + newMat[p][i + 1:]
                
                print('newMat[p][:i]: ' + str(newMat[p][:i]))
                print('newMat[p][i]: ' + str(newMat[p][i]))
                print('newMat[p][i + 1]: ' + str(newMat[p][i + 1:]))
                
                
                # print('subArr: ' + str(subArr))
                # returnMat.append(subArr)
                
                p += 1
                t -= p
        else:
            # returnMat.append(newMat[i])
            aa = 1
            
        returnMat.append(subArr)
        i += 1
    
    print('newMat flipCol start: ' + str(returnMat))
    return returnMat


def flippingMatrix(matrix):
    # Write your code here
    
    n = math.floor(len(matrix) / 2)
    result = 0
    m = 0
    p = 0
    
    newMat = flipRow(matrix)
    newMat = flipCol(newMat)
    finalMat = flipRow(newMat)
    
    while m < n:
        p = 0
        while p < n:
            # print('newMat[' + str(m) + '][' + str(p) + '] = ' + str(newMat[m][p]))
            result += finalMat[m][p]
            p += 1
        m += 1

    return result



if __name__ == '__main__':

    matrix = [[1,2],[3,4]]
    matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix3 = [[11,2,43,24],[5,0,7,38],[59,10,151,125],[13,94,615,116]]
    matrix4 = [[15,41,44,38],[20,75,50,14],[99,44,11,22],[10,54,32,12]]

    result = flippingMatrix(matrix4)
        
    print(result)















