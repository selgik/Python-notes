#note005_if, for, while.py

########## 1. IF
#1) If condition: statement
#Tip: INDENTATION MATTER!!! Witout indentation, system will give an error. In Visual Studio, codes will have lines to indicate flow.
weather = "rain"
if weather == "rain":
    print("It's raining, take umbrella!")
elif weather == "snow":
    print("It's snowing, take umbrella and gloves!")
else:
    print("Good weather! Have a nice day!")

#2) User can input the condition
weather = input("What's the weather today?")
if weather == "rain" or weather == "snow" : print("Take umbrella!")
#if weather == ("rain" or "snow") didn't work out, when I typed "snow".
elif weather == "storm": print("Stay at home!")
else: print("Good weather! Have a nice day!")

#3) input() will store data as Strings. use Int() to convert into integer.
temp = int(input("What's the temperature outside?"))
if temp >= 30:
    print("it's quite hot outside, be careful!")
elif temp<30 and temp >=10:
    print("it's good weather for outdoor activity!")
elif 0 <= temp <10:
    print("it's getting chilly, bring jumper!")
else:
    print("it's freezing outside!")

########## 2. FOR
#1) Used for loops
#Let's say you need to print the queue number for customers. Ex) we have 5 customers, you want below result
print("Your queue number is 1")
print("Your queue number is 2")
print("Your queue number is 3")
print("Your queue number is 4")
print("Your queue number is 5")

#2) Using for, you can write as below and obtain the same result:
For queue in [1, 2, 3, 4, 5]: # or For queue in range(1, 6):
    print("Your queue number: {}" .format(queue))

#3) Same format for strings
For guests in ["John", "Ella", "Tom"]:
    print("{}, your coffee is ready!" .format(guests))

########## 3. WHILE
#1) While condition is met, loop
#Let's say a coffee shop is calling customer when coffee's ready for 5 times and throw away if no one appears.

guest = "Jenny"
turn = 5

while turn >= 1:
    print("{}, your coffee is ready! {} calling time left!" .format(guest, turn-1))
    turn -= 1
if turn == 0:
    print("Coffee is thrown away...")
    
#2) Loop forever: while True
guest = "Adam"
turn = 1

while True:
  print("{}, your coffee is ready! calling you {}th time!" .format(guest, turn))
  turn += 1
  
#Break loop if turn hits 10
guest = "Adam"
turn = 1

while True:
  print("{}, your coffee is ready! calling you {}th time!" .format(guest, turn))
  turn += 1
  if turn >= 11:
      break

#3) loop with strings
#call the guest, check cust's name and compare cust vs guest. If cust! = guest, repeat the process.
guest = "Martin"
cust = "Doe"

while cust != guest:
    print("{}, your coffee is ready!" .format(guest))
    cust = input("what's your name?")
    
#now let's ask guest's name first and compare whether their coffee is ready. 
ready = "Pawel"
guest = input("what is your name?")

while guest != ready:
    print("It's not yet your turn")
    guest = input("what is your name?")  #print(guest) gave infinite results hence wrote as above.
if guest == ready:
    print("Your coffee is ready!")
    
########## 4. CONTINUE, BREAK 
#continue: skips its queue in the loop, break: breaks the loop
#There are 10 students in the clase. 2 students are absent, 1 student forgot the book. 

absent = [2, 6]
forgotb = [8]

for studetns in range(1,11):
    if students in absent:
        continue
    elif studetns in forgotb:
        print("{}, come to my office!" .format(students))
        break 
    print("{}, please read next paragraph" .format(students))
  
########## 5. MANIPULATING FOR
#1) Make changes to the list, in ex. instead of having 1, 2, 3,... have 1001, 1002, 1003...
my_list = [1,2,3,4,5]
my_list = [i + 1000 for i in my_list]    # my_list = my_list + 1000 will give errors. 
print(my_list)                           # result is [1001, 1002, 1003, 1004, 1005]

#2) calculate length of the strings within the list
my_list = ["Marin", "Avicci", "Stickmen", "BTS"]
my_list = [len(i) for i in my_list]

#3) change str to upper/lower cases
my_list = ["Marin", "Avicci", "Stickmen", "BTS"]
my_list = [i.upper() for i in my_list]
my_list = [i.lower() for i in my_list]

########## 6. EXERCISE 
# Imagine you are an Uber driver. Everyday you get assigned with 50 customers.
# Each customer's ride duration ranges from 5min - 50 min (randomly). 
# But you want to only accept customers of that duration range between 5min - 15 min
# Write codes which will show as below:
#   [o] 1th customer (duration: 14 minutes)
#   [ ] 2th customer (duration: 45 minutes)
#   [o] 3th customer (duration: 9 mintues) ...

#1) First try
from itertools import count
import random
guests = list(range(1, 51))
duration = [random.randrange(5, 51) for i in range(5, 51)]    #ref1
index = 0

for (g, d) in zip(guests, duration):    #ref2
    if 5<= d <=15:
        print("[{}] {}th guest (duration:{} minutes)" .format("o", g, d))
        index += 1
    else:
        print("[{}] {}th guest (duration:{} minutes)" .format(" ", g, d))

print("Total {} guests had a ride" .format(index))

# Failure notes:
# ref1: I wanted to make a random list containing duplicates between 5-50.
#       First, I created list and then use random.shuffle(list) but I realized this will simply shuffle list without duplicates.
#       Next, I tried list = random.sample(range(5,51), 46) but this ultimately gave the same result, containing no duplicates.
#       So I created ref1. Without for i in range(5,51) part, this will only give random 1 number, not a list.
# ref2: First, I wrote as below but realized it's nested loop. Results had multiple customers numbers. 
#       for guests in range(1,51):
#           for duration in ... 
#       I wanted to give pararell/multiple for, not nested for. Hence found for (a, b) in zip(x, y)

#2) Right answer
from random import *
cnt = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5<= time <=15:
        print("[o] {0}th guest (duration:{1} minutes)" .format(i, time))
        cnt += 1
    else:
        print("[ ] {0}th guest (duration:{1} minutes)" .format(i, time))
print("Total {0} guests had a ride" .format(cnt))

#What's better here: codes are shorter and clearer
