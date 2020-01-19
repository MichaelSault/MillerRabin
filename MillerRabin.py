#Implementation of Miller-Rabin probabilistic primality testing algorithm
#Wednesday, November 6, 2019

#Name: Michael Sault
#Writen for Python 3

import random

def miller_rabin(n):
    #check if n is a 14 bit integer
    #assume a 14-bit integer can be any integer >16448 (as the first 13 bits could be 0)
    if (n <= 16447):
        
        
        #check if it is 2 or 3, these are too small to work with this function, but are prime
        if (n==2)or(n==3):
            print ("The Probable Prime is:" , n) 
            return True
        elif (n % 2 == 0): #check if it is even and therefor prime
            print ("Composite:",n)
            return False
    
        r = 0
        d = n - 1
    
        while d % 2 == 0:
            r = r+1
            d = d//2
            
        for _ in range(5): #confidence t=5
            a = random.randrange(2, n - 1)
            b = pow(a, d, n)
            if (b == 1) or (b == n - 1):
                continue
            for _ in range(r - 1):
                b = pow(b, 2, n)
                if b == n - 1:
                    break
            else:
                print ("Composite:", n)
                return False
        print ("Probably Prime")
        print ("The Probable Prime is:" , n) 
        return True
    else:
        print ("Not a 14-bit Integer!")
        return False
   

#generate random 14-bit integers and test them to see if prime
prime_found = False

while (prime_found == False):
    n = random.randint(2, 16447)
    prime_found = miller_rabin(n)