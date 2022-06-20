#note002_operator.py

#1. Operators (arithmetic) 
print(2*3)              # result is 6
print(2**3)             # result is 8, because --> 2^3
print(5/3)              # result is 1.666666...
print(5//3)             # result is 1, because --> 5/3 = 1.666 --> quotient is 1.
print(5%3)              # result is 2, because --> 5/3 --> 5=(3*1)+2 --> remainder is 2.

#2. Operators (boolean) 
print(10>3)             # True
print(10>5>3)           # True, because --> 10>5 is True and 5>3 is True.
print(4>=7)             # False
print(3==3)             # True, because --> here, first value is compared with the second value. They are the same, hence true.
print(4==2)             # False
print(3+4==7)           # True
print(3=3)              # This will give an error message! Wrong operator!

print(1!=3)             # True
print(not(1!=3))        # False, because --> print(not(True))

print((3>0) and (3<5))  # True
print((3>0) & (3>7))    # False
print((3>0) or (3>5))   # True
print((3>0) | (3>5))    # True

#3. Operators (variable) 
number = 4+2*5
print(number)           # result is 14
number = number +2
print(number)           # result is updated to 16
number +=2              # same as number = number+2
number -=8              # same as number = number-8
number *=2              # same as number = number*2
number /=4              # same as number = number/2
number %=3              # same as number = number%3
print(number)           # result is 2, because --> (16+2-8)*2/4=5 --> 5=(3*1)+2 remainder is 2

#4. Functions
print(abs(-3))          # result is 3 --> returns absolute value
print(pow(4,2))         # result is 16 --> 4 power of 2 (4^2)
print(max(5,12))        # result is 12. Works with multiple value such as print(max(1,5,2,44))
print(min(5,12))        # result is 5
print(round(3.14))      # result is 3
print(round(4.677))     # result is 5

#5. Mathematic function
from math import *
print(floor(4.99))      # result is 4. Get rid of remainder
print(ceil(3.14))       # result is 4. Round up!
print(sqrt(16))         # result is 4. Squre root of 16

#6. Random function
from random import *
print(random())             # returns random value between 0.0 - 1.0 (excl 1.0) --> ex. 0.1324552..
print(random()*10)          # returns random value between 0 - 10 (excl 10) --> ex. 3.2453421..
print(int(random()*10))     # returns random value between 0 - 10 (excl 10) in INT format --> ex. 4
print(int(random()*10)+1)   # returns random value between 1 - 11 (excl 11) in INT format --> ex. 10

print(randrange(1,11))      # returns random value between 1 - 10
print(ranint(1,10))         # returns random int vetween 1 - 10 including both 1 and 10.

