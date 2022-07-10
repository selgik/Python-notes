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

# result of 22: You have depositied 300, now your balance is 1300.
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



