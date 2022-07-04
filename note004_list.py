#note004_list (dictionary, tuples, set, data structure).py

#1. List
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
print(num_list.pop())                     #pop removes the last item in the list: result is 33
print(numb_list)                          #result is [10, 24, 15, 20]
num_list.sort()                           #sort() will sort list ASC order    
print(num_list)                           #result is [10, 15, 20, 24]
num_list.reverse()                        #reverse() will sort list DESC order
print(num_list)                           #result is [24, 20, 15, 10]

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

#2. Dictionary

#3. Tuple

#4. Set




