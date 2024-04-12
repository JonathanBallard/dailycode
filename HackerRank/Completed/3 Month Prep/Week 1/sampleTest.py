
#~ -----------------------------------------------------------------

# Name:         Jonathan Ballard
# Date:         4.11.24
# Site:         HackerRank
# Section:      3 Month Prep - Week 1
# Problem:      FizzBuzz (Sample Test)

#~ -----------------------------------------------------------------




def fizzBuzz(n):
    i = 1
    
    while(i <= n):
        if(i % 3 == 0):
            if(i % 5 == 0):
                print('FizzBuzz')
            else:
                print('Fizz')
        elif(i % 5 == 0):
            print('Buzz')
        else:
            print(i)
        i += 1





if __name__ == '__main__':

    n = 20
    
    fizzBuzz(n)


