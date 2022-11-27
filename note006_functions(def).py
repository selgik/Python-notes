#note006_functions(def).py 

########## 1. FUNCTIONS
#1) Let's create a baic function (similar to customed function in VBA) 
def open_account():
  print("New account has been generated")

# This will simply create a function. If above is run, nothing will be printed.
# In order to get a result, you need to call the function with --> function()

def open_account():
  print("New account has been generated")
open_account()                           # result: New account has been created

#2) Let's add arguments
def deposit(balance, money):
  print("You have depositied {}, now your balance is {}." .format(money,balance))
  #or, you can also write as print("Deposit received. Your current balance is {}." .format(money+balance))
  return balance + money                # failure note: balance = balance + money
  
balance = 1000
balance = deposit(balance, 300)         # failure note: print(balance, 100) --> result is: You have depositied 300, now your balance is 1000.
print(balance)

# result of 22: You have depositied 300, now your balance is 1000.
# result of 23: 1300

#3) use two functions. 
def deposit(balance, money):
  print("Deposit received. Your current balance is {}." .format(money+balance))
  return balance+money # ref1  

def withdraw(balance, money):
  if money <= balance:
    print("Your have withdrawn {}, current balance is {}." .format(money, balance-money))
    return balance-money
  else:
    print("Your do not have enough money to withdraw")
    return balance

balance = 1000
balance = deposit(balance, 300)
balance = withdraw(balance, 500)
print(balance)

#ref1: without that line, first function deposit() will be done but next function withdraw() will not be done, 
#      as balance value is not stored and error message will show balance as 'NoneType'.

#4) return multiple values (in tuples)
def night_withdraw(balance, money):
  comission = 50
  return comission, balance-money-comission       #this will be tuple.

balance = 1000
comission, balance = night_withdraw(balance, 300) #valeus returned as a result of night_withdraw(balance, money) are (comission, balance<-which is balance-comission-money)
print("comission is {}, current balance is {}." .format(comission, balance))

########## 2. DEFAUT ARGUMENT
#1) create profiles for new hires
def profile(name, age, dept):
  print("Name: {0}, age: {1}, department: {2}" \   #if sentence is getting longer, we can use \to organize codes.
        .format(name, age, dept))                  #same as: print("Name: {0}, age: {1}, department: {2}" .format(name, age, dept)) 
profile("Ron K.", 25, "Sales")                        
profile("Jim A.", 43, "R&D")
profile("Son E.", 33, "Admin")

#2) imagine all new hires are 30 and belong to Sales dept. Instead of writing same arguments repetitively, defulat argument can be used as below:
def profile(name, age = 30, dept = "Sales"):
  print("Name: {0}, age: {1}, department: {2}" .format(name, age, dept))  
profile("Ron K.")                        
profile("Jim A.")
profile("Son E.")

########## 3. KEYWORD ARGUMENT
def profile(name, age, dept):
  print("Name: {0}, age: {1}, department: {2}" .format(name, age, dept))  

profile(detp = "Finance", name = "Terry R.", age = 45) #order does not matter.

########## 4. ARBITRARY ARGUMENT
#1) create profiles for new hires
def profile(name, age, c_lang1, c_lang2, c_lang3, c_lang4, c_lang5):
  print("Name: {0}, age: {1}" .format(name, age), end=" ")  #end= " " allows next line to print without new line.
  print("Computer languages:" + c_lang1, c_lang2, c_lang3, c_lang4, c_lang5)
 
profile("Tadek", 30, "Python", "SQL", "R", "C", "C++")
profile("Ukasz", 24, "Java", "Python", " ", " ", " ")

#Problem: we need to create a profile for Ukasz who can only do 2 computer languages.
#         also, what if Tadek happens to obtain more computer language skills? We need more flexible codes for these.

#2) use arbitrary argument
def profile(name, age, *c_lang):
  print("Name: {0}, age: {1}" .format(name, age), end=" ")  #end= " " allows next line to print without new line.
  for lang in c_lang:
    print(lang, end= " ") #without end= " ", all c_lang values will be printed in new line
  print()                 #without print(), Ukeasz's profile will be crated in the same line as Tadek's
  
profile("Tadek", 30, "Python", "SQL", "R", "C", "C++", "Java")
profile("Ukasz", 24, "Java", "Python")

########## 5. GLOBAL VS LOCAL VARIABLES
#1) global variable: variables, created outside the function
#   local variable: variables, created inside the function
 
candy = 15  
def candy_checker(child):
  candy = 10
  candy = candy - child
  print("[Inside Function] {} candies left." .format(candy))

print("{} total candies." .format(candy))
candy_checker(4)
print("{} remaining candies." .format(candy))
  
#results:
#15 total candies. --> this is using global variable candy = 15
#[Inside Function] 6 candies left. --> this is using local variable candy = 10
#15 remaining candies.  --> this is using global variable candy = 15

#2) rewrite above using global variable
candy = 15  
def candy_checker(child):
  globa candy
  candy = candy - child
  print("[Inside Function] {} candies left." .format(candy))

print("{} total candies." .format(candy))
candy_checker(4)
print("{} remaining candies." .format(candy))
  
#results:
#15 total candies. --> this does not go through function hence still 15.
#[Inside Function] 11 candies left. --> 15-4=11
#11 remaining candies.  --> candy's value is stored as 11 from previous execution.

#tip: 
#apparently, it is not easy to manage global variable hence it is not recommended to use them. Instead, 

#3) recommended:
candy = 15  
def candy_checker(candy, child):
  candy = candy - child
  print("[Inside Function] {} candies left." .format(candy))
  return candy  #re2

print("{} total candies." .format(candy))
candy = candy_checker(candy, 4) #ref3
print("{} remaining candies." .format(candy))
  
#results:
#15 total candies. --> this does not go through function hence still 15.
#[Inside Function] 11 candies left. --> by executing line 148, print function of line 144 gets executed
#11 remaining candies.  --> as line 148 was executed, candy value was updated to 11. Hence result is 11. 
  
########## 6. EXERCISE
# create a function that calculates standard weight for female (height_m * height_m * 21) and male (height_m * height_m * 22)
# use two arguments, height and gender. Standard weight should have max two decimal places. 

def standard_wcal(height, gender):
  if gender == "female":
    return height * height * 21
  else: 
    return height * height * 22
  
height = 160
gender = "female"
standard_wg = round(standard_wcal(height, gender)/10000, 2)
#or: standard_wg = round(standard_wcal(height/100, gender), 2)
print("Standard weight for {} with {} cm height is {}." \
      .format(gender, height, standard_wg)
      
  
