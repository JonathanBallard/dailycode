
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.9.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 1
# Problem:      camelCase

#~ -----------------------------------------------------------------


#^ Description
# Each line of the input file will begin with an operation (S or C) 
# followed by a semi-colon followed by M, C, or V 
# followed by a semi-colon 
# followed by the words you'll need to operate on.
# The operation will either be S (split) or C (combine) 
# M indicates method, C indicates class, and V indicates variable
# In the case of a split operation, the words will be a camel case method, class or variable name 
# that you need to split into a space-delimited list of words starting with a lowercase letter.
# In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters 
# that you need to combine into the appropriate camel case String. 
# Methods should end with an empty set of parentheses to differentiate them from variable names.
# For each input line, your program should print either the space-delimited list of words (in the case of a split operation) 
# or the appropriate camel case string (in the case of a combine operation).

#^-------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3


import sys


def readLine(line):
    # sys.stdout.write('readLine ' + line + '\n')
    split = line.split(';')
    command = split[0]
    type = split[1]
    words = split[2]
    
    words = words.strip()

    # splitWord = words.split('\n')
    # words = splitWord[0]
    
    
    if command == 'C':
        line = combineWords(type, words)
    elif command == 'S':
        line = splitWords(type, words)
    return line


def combineWords(type, words):

    i = 0
    length = len(words)
    
    while(i < length):
        if(words[i] == ' ' and i + 1 <= length):
            split = words.split(' ')
            
            if(type == 'M'):
                newSplit1 = split[1][1:]
                words = split[0] + words[i+1].capitalize() + newSplit1
                
            elif(type == 'V'):
                words = split[0] + split[1].capitalize()
                j = 2
                splLength = len(split)
                
                if(splLength > 2):
                    while j < splLength:
                        words += str(split[j].capitalize())
                        j += 1
                
            elif(type == 'C'):
                newSplit1 = split[1][1:]
                words = split[0].capitalize() + words[i+1].capitalize() + newSplit1
            
            length = len(words)
        
        i += 1
        
    # handle methods
    if(type == 'M'):
        spl = words.split('\n')
        words = ''.join(spl[0]) + '()'
        return str(words) + '\n'

    
    # handle vars
    if(type == 'V'):
        return str(words) + '\n'
    
    # handle classes
    if(type == 'C'):
        words = ''.join(words[0].capitalize()) + words[1:]
        return str(words) + '\n'


def splitWords(type, words):
    
    length = len(words)
    i = 0
    
    # add spaces, and lowercase necessary characters
    while i + 1 < length:
        
        wordStr = ''
        
        if words[i] == words[i].upper() and not i == 0:
            char = words[i].lower()
            x = slice(i)
            words1 = words[x]

            x2 = (length * -1) + (i + 1)
            words2 = words[x2:]
            
            wordStr = ''.join(words1)
            wordStr = wordStr + ''.join(' ') + ''.join(char)
            words = wordStr + ''.join(words2)
            
        i += 1
    
    words = words.lower()
    
    # handle methods
    if(type == 'M'):
        split = words.split('()')
        return str(split[0]) + str(split[1]) + '\n'
    
    # handle vars
    if(type == 'V'):
        return str(words) + '\n'
    
    # handle classes
    if(type == 'C'):
        return str(words) + '\n'


if __name__ == '__main__':
	
    lines = ['S;V;iPad', 'C;M;mouse pad', 'C;C;code swarm', 'S;C;OrangeHighlighter', 'C;V;mobile phone', 'S;M;plasticCup()']
    linesS = ['S;V;iPad', 'S;C;OrangeHighlighter', 'S;M;plasticCup()']
    linesC = ['C;M;mouse pad', 'C;C;code swarm', 'C;V;mobile phone']

    lines2 = ['C;V;can of coke', 'S;M;sweatTea()', 'S;V;epsonPrinter', 'C;M;santa claus', 'C;C;mirror']
    
    for line in lines:
        output = readLine(line)
        #sys.stdout.write(output)
        print(output)
        







