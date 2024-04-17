
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.14.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 2
# Problem:      Grading Students

#~ -----------------------------------------------------------------




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    roundedGrades = []
    
    for el in grades:
        if el < 38:
            roundedGrades.append(el)
        elif el % 5 == 0:
            roundedGrades.append(el)
        else:
            i = math.ceil(el + 1)
            
            if i % 5 == 0:
                roundedGrades.append(i)
                
            elif ((i + 1) % 5) == 0:
                roundedGrades.append(i + 1)
            else:
                roundedGrades.append(el)
            
    return roundedGrades

if __name__ == '__main__':

    grades = [39,100,0,57,55,98,99,97,66]

    result = gradingStudents(grades)
    
    print(result)
















