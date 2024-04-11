
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
    # sys.stdout.write('readLine -->  ' + line + '\n')
    print('readLine -->  ' + line + '\n')
    split = line.split(';')
    command = split[0]
    type = split[1]
    words = split[2]

    splitWord = words.split('\n')
    words = splitWord[0]

    if command == 'C':
        line = combineWords(type, words)
    elif command == 'S':
        line = splitWords(type, words)
        return line


def combineWords(type, words):

    i = 0
    words = list(words)
    length = len(words)

    # remove spaces, and uppercase necessary characters
    while i < length:
        if words[i] == ' ' and words[i + 1] and not i == 0:
            words[i + 1].upper()
            length = len(words)

            x = slice(i)
            words1 = words[x]

            x2 = (length * -1) + (i + 1)
            words2 = words[x2:]

            words = words1 + words2

        i += 1

        # handle methods
    if(type == 'M'):
        return words + '()'

        # handle vars
    if(type == 'V'):
        return words

        # handle classes
    if(type == 'C'):
        words[0].upper()
        return words

def splitWords(type, words):
    
    i = 0
    words = list(words)
    length = len(words)

    # add spaces, and lowercase necessary characters
    while i < length:
        
        wordStr = ''
        
        if words[i] == words[i].upper() and not i == 0:
            
            words[i].lower()
            
            # backup = words[i]
            x = slice(i)
            words1 = words[x]

            x2 = (length * -1) + (i)
            words2 = words[x2:]
            
            # words[i] = backup
            # print('words[i]')
            # print(words[i])

            # print('i')
            # print(i)
            
            wordStr = ''.join(words1)
            wordStr = wordStr + ''.join(' ')
            wordStr = wordStr + ''.join(words[i])
            wordStr = wordStr + ''.join(words2)
            words = str(wordStr)
            
            print('end')
        
        i += 1


    # handle methods
    if(type == 'M'):
        split = words.split('()')
        return split[0]

    # handle vars
    if(type == 'V'):
        return words

    # handle classes
    if(type == 'C'):
        return words



if __name__ == '__main__':
	
    lines = ['S;V;iPad\n', 'C;M;mouse pad\n', 'C;C;code swarm\n', 'S;C;OrangeHighlighter']

    # lines = ['S;C;OrangeHighlighter']

    for line in lines:
        output = readLine(line)
        #sys.stdout.write(output)
        print(output)
        







