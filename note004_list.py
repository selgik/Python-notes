#note004_list (dictionary, tuples, set, data structure).py

#1. List []
#Similar to arrays, multiple values can be stored under one variable in python.
#Instead of below (line 6:8) use lists (line 9)
var1 = 10
var2 = 15
var3 = 20
num_list = [10, 15, 20]
str_list = ["love", "hate", "surrow"] 
print(num_list)                           #result is [10, 15, 20]
print(num_list[0])                        #result is 10
print(str_list.index[2])                  #result is surrow

#Maniuate list by adding, removing, sorting or counting.
num_list.append(33)
print(num_list)                           #append will add value in the end of the list: result is [10, 15, 20, 33]
num_list.insert(1, 24)                    
print(num_list)                           #insert will add value in the designated place: result is [10, 24, 15, 20, 33]
print(num_list.pop())                     #pop removes the last item in the list which is, 33. print(num_list) will be then [10, 24, 15, 20]
print(num_list.pop(2))                    #removed item will be index#1 which is 15. print(num_list) will be then [10, 24, 20]

num_list.insert(2,15)
print(numb_list)                          #result is [10, 24, 15, 20]
num_list.sort()                           #sort() will sort list ASC order    
print(num_list)                           #result is [10, 15, 20, 24]
num_list.reverse()                        #reverse() will sort list order in reverse way. Result will be [20, 15, 24, 10]
num_list.sort(reverse=True)               #this will sort list values in desc order. Result will be [24, 20, 15, 10]

# NOTE: print(num_list.sort()) did not work out. It returned "None". 
# My question is why? Why can't I directly modify and see the result?
# This is because sort() is modifying function only. It is NOT a list itselt, hence no list to return.
# Credit: https://stackoverflow.com/questions/64287516/why-cannot-directly-use-printsomething-sort
  
str_list.append("love") 
print(str_list)                           #result is ["love", "hate", "surrow", "love"]
print(str_list.count("love"))             #result is 2

num_list.extend(str_list)                 #extend combines the lists.
print(num_list)                           #result is [10, 24, 15, 20, "love", "hate", "surrow", "love"] <-- two different data types can exist in the list. 

num_list.clear()
print(num_list)                           #result is []

#2. Dictionary {}
#we have key and corresponding value in dictionary. Key is unique. 
dic = {3:"Kim", 5:"Lee", 10:"Tan"}        #keys are 3, 5, 10. They are integer but do not have to be. 
dic2 = {"A3":"J", "A5":"T", "A10":"S"}    #keys like this, can be strings too.

print(dic2["A3"])                         #result is J
print(dic[3])                             #result is Kim
print(dic.get(3))                         #same as above, result is Kim
print(dit[0])                             #result is KeyError. There is no 0 in key. (only 3, 5 and 10)
print(dic.get(0))                         #result is None. For this code, program will further execute codes unlike print(dic[0]) where program will simply end.
print(dic.get(0, "Available"))            #result is Avaiable. If there is no value for key=0, "Available" will show up.
print(3 in dic)                           #result is True. There is 3 in dic.
print(4 in dic)                           #result is False. There is no 4 in dic.

#Maniuate dictionary by adding, removing or sorting.
dic[12] = "Park"                          #add key 12 = "Park"
print(dic)                                #result is {3:'Kim', 5:'Lee', 10:'Tan', 12:'Park'}
del dic[5]                                #delete key 5 and its value
print(dic)                                #result is {3:'Kim', 10:'Tan', 12:'Park'}
print(dic.keys())                         #returns keys only. Result is dict_key([3,10,12])
print(dic.values())                       #returns values only. Result is dict_values(['Kim', 'Tan', 'Park'])
print(dic.items())                        #result is dict_items([(3, 'Kim'), (10, 'Tan'), (12, 'Park')])

dic.clear()                               #clear the dictionary
print(dic)                                #result is {}

#3. Tuple ()
# In tuple, we CANNOT add or edit items. Need to change Type first before making any changes to Tuples.
menu = ("Burger", "Dimsum", "Kimchi")
print(menu)                               #result is ('Burger', 'Dimsum', 'Kimchi')
print(menu[0])                            #result is Burger
# Usage: instead of line 77-80, we can use tuple like line 82-83:
name = "Kim"
age = 25
hobby = "boxing"
print(name, age, hobby)

(name, age, hobby) = ("Kim", 25, "boxing")
print(name, age, hobby)                   # codes are shorter, result is Kim 25 boxing

#4. Set {}
#In set, duplicates are not alloweded. Also, order is ignored.
set1 = {1, 3, 5, 5, 5, 6}
print(set1)                               #result is {1, 3, 5, 6}

#we can do different types of JOIN with Sets.
grade1 = {"history", "math", "music"}
grade2 = {"math", "biology", "geography"}

print(grade1 & grade2)                    #Inner Join: result is {'math} 
print(grade1.intersection(grade2))        #Inner Join: result is {'math}
print(grade1 | grade2)                    #Outer Join: result is {'history', 'music', 'math', 'biology', 'geography'}
print(grade1.union(grade2))               #Outer Join: result is {'history', 'music', 'math', 'biology', 'geography'}
print(grade1-grade2)                      #Difference(set-intersection): result is {'history', 'music'}
print(grade1.difference(grade2))          #Difference(set-intersection): result is {'history', 'music'}
    
#add or remove:
grade2.add("physics")                     #add value
grade2.remove("geography")                #remove value
  
#5. Change in data structure  
print(grade1, type(grade1))               #type() returns the data type. result is {'history', 'math', 'music'} <calss 'set'>
grade1 = list(grade1)                     #changes data type to list
grade2 = tuple(grade2)                    #changes data type to tuple
grade2 = set(grade2)                      #changes data type back to set
  
#6. Exercise
#Imagine 25 students have applied for school lottery. I need to select 4 people (no duplicates) for 1st price of computer and 2nd place for coffee. 
#1) First try

id = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
from random import *
shuffle(id)
print("Winner of 1st place: " + str(sample(id, 1)) +
      "\n 2nd place winners: " + str(sample(id, 3)))

# although I obtained expected result, there are two problems with above codes
# Failure note: I had to write id numbers manually. Imagine 100 students have signed up? It is manual work also easy to make mistakes. 
#               Also, using sample() functions twice can result in returning duplicate values. 
#               Since requirement was clear that I should NOT pick the same person for 1st and 2nd place, I need to make changes to the codes.

#2) Right answer
users = range(1, 26)                      #range() will create the same value as id above.
users = list(users)                       #since range is created, need to change to list. 
print(type(users))                        #result is <class 'list'>
# Using above, I do not have to manually type the id numbers.

from random import *
winners = sample(users, 4)
#No need to do shuffle. Everytime I run function sample(), it will pick random value anyway. 
#By using sample(users, 4) no duplicate winner(for 1st place and 2nd place) will be selected.

print("Winner of 1st place is {}" .format(winners[0]) +
      "\n2nd place winners are {}" .format(winners[1:]))

