# import available
'''
from math import gcd

gcd(a, b)
'''
'''
def GCD(a,b): 
    if(b==0): 
        return a 
    else: 
        return GCD(b,a%b) 
'''

'''
def GCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 
'''

'''
def GCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 

'''
