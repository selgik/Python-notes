#note007_print2(input,output).py

########## 1. PRINT, STDOUT, STDERR
#1) Various ways to print 
print("Apple", "Juice")                     #result is Apple Juice
print("Apple" + "Juice")                    #result is Apple Juice
print("Apple", "Juice", sep ="-")           #result is Apple-Juice
print("Apple", "Juice", sep =",", end="! ")
print("Toast")                              #result is Apple, Juce! Toast --> thanks to end="", line will not be changed.

#2) STDOUT, STDERR
import sys
print("Apple", "Juice", file=sys.stdout)    #result is Apple Juice
print("Apple", "Juice", file=sys.staderr)   #result is Apple Juice

#When running above codes in Visual Studio, we won't see any difference
#When to use: when we run a program with long codes, we may need to track logs.
#             in ex, in what time I did A, and result was B etc. 
#             running stdout will show the contents. stderr will show errors related to the codes.

#3) STANDARD INPUT
answer = input("Enter your answer")
print("You have entered" + answer) 
type(answer)                                #always String value
# When we get value from input(), value will always be stored as String. 

########## 2. FORMATTING
#1) print dictionary items in reader-friendly format:
results = {"Math": 5, "English": 80, "Coding": 95}
for subject, score in results.items():
    print(subject, score)
#result is:
#Math 5
#English 80
#Coding 96

results2 = {"Math": 5, "English": 80, "Coding": 95}
print(results2)
#result is: 
#{'Math': 5, 'English': 80, 'Coding': 95}

#2) Re-organize so that it's aligned on the right side
results = {"Math": 5, "English": 80, "Coding": 95}
for subject, score in results.items():
    print(subject.ljust(8), str(score).rjust(4), sep =" :")      #ljust: keep 8places on the left (rjust for right side)
#result is:
#Math    :   5
#English :  80
#Coding  :  96

#3) Let's insert 0 to the blank places
for number in range(1,21):
  print("Your queue number is: " + str(number).zfill(3))
#result is:
#Your queue number is: 001
#Your queue number is: 002
#Your queue number is: 003
#...
#Your queue number is: 020

########## 3. VARIOUS OUTPUT FORMATS
#1) keep 10 empty places -> right align(write value aligning on the right side) -> value is 800
print("{0: >10}" .format(800))    #result is '       800'

#2) add +- sign 
print("{0: >+10}" .format(800))           #result is '      +800'
print("{0: >+10}" .format(-800))          #result is '      -800'
# print("{0: >10}" .format(+800)) won't show result as +800. It will show 800.

#3) align left, fill empty places with underbar
  print("{0:_<+10}" .format(+800))        #result is +800______

#4) add , every three digits.
print("{0:,}" .format(123123123))         #result is 123,123,123

#5) add , every three digits & add +- sign.
print("{0:+,}" .format(123123123))        #result is +123,123,123

#6) add , every three digits & add +- sign & keep 30 places and fill with ^ for empty places
print("{0:^>+30,}" .format(123123123))    #result is ^^^^^^^^^^^^^^^^^^^^+123123123
print("{0:^<+30,}" .format(123123123))    #result is +123123123^^^^^^^^^^^^^^^^^^^^

#7) print decimal places:
print("{0:f}" .format(3/4))               #result is 0.750000
#print("{0}" .format(3/4))                #result is 0.75

#8) print to x decimal places:
print("{0:.3f}" .format(3/4))             #result is 0.750
