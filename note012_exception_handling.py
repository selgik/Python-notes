#note012_exception_handling.py

########## 1. EXCEPTION HANDLING
#1) Think about simple calculator as below:

print("Let's divide numbers")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print("{} divided by {} is {}" .format(num1, num2, int(num1/num2)))

# what if user enters string value? or 0?
# in above codes, error message will print out within the long text, being misleading.
# by using exception handling, erorrs can be printed out in much clearer way.  

try:
  print("Let's divide numbers")
  num1 = int(input("Enter your first number: "))
  num2 = int(input("Enter your second number: "))
  print("{} divided by {} is {}" .format(num1, num2, int(num1/num2)))
except ValueError: # ValueError is when you enter string value in num1 or num2. Copy the keyword.                 
  print("You have entered wrong value")
except ZeroDivisionError as err:  # ZeroDivisionError is when you enter 0. Copy the keyword.     
  print(err)

#when ValueError occurs, "You have entered wrong value" will print out.
#when ZeroDivisionError occurs, "division by zero" will print out.

#2) Let's use another example. We will make list this time:

try:
  print("Let's divide numbers")
  nums = []
  nums.append(int(input("Enter your first number: ")))
  nums.append(int(input("Enter your second number: ")))
  nums.append(int(nums[0]/nums[1]))
  print("{} divided by {} is {}" .format(nums[0], nums[1], nums[2]))
except ValueError:                
  print("You have entered wrong value")
except ZeroDivisionError as err:  
  print(err)

# let's pretend that I forgot to append nums[0]/nums[1]. IndexError will appear.
# we can use except: to handle rest errors:

try:
  print("Let's divide numbers")
  nums = []
  nums.append(int(input("Enter your first number: ")))
  nums.append(int(input("Enter your second number: ")))
  print("{} divided by {} is {}" .format(nums[0], nums[1], nums[2]))
except ValueError:                
  print("You have entered wrong value")
except ZeroDivisionError as err:  
  print(err)
except:
  print("Unknown error has occured!")

#if I want to know what kind of error it is, use below instead:
except Exception as err:
  print(err)
  
  
########## 2. CREATE AND MANAGE ERRORS:
# add constraints and manage errors:

try:
  print("Let's divide numbers")
  num1 = int(input("Enter your first number: "))
  num2 = int(input("Enter your second number: "))
  if num1 >=10 or num2 >= 10:
      raise ValueError
  print("{} divided by {} is {}" .format(num1, num2, int(num1/num2)))
except ValueError:
  print("Please enter value less than 10")


########## 3. USER DEFINED EXCEPTION HANDLING
#ValueError or ZeroDivisionError are Python defined errors.
#1) we can also create our own errors and define.

class SylviaError(Exception):
    pass
try:
  print("Let's divide numbers")
  num1 = int(input("Enter your first number: "))
  num2 = int(input("Enter your second number: "))
  if num1 >=10 or num2 >= 10:
      raise SylviaError
  print("{} divided by {} is {}" .format(num1, num2, int(num1/num2)))
except ValueError:
  print("Please enter value less than 10")
except SylviaError:
  print("Let's try again!")
  
# in this case if error occurs - if either num1 or num2 is bigger than 10:
#"Let's try again!" will print out instead of "Please enter value less than 10".

#2) let's add message for error:

class SylviaError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    print("Let's divide numbers")
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    if num1 >=10 or num2 >= 10:
        raise SylviaError("Check what you've entered: {}, {}" .format(num1, num2))
    print("{} divided by {} is {}" .format(num1, num2, int(num1/num2)))
except ValueError:
    print("Please enter value less than 10")
except SylviaError as err:
    print("Let's try again!")
    print(err) 

#when error occurs, two lines will be printed out:
#Let's try again!
#Check what you've entered: num1, num2


########## 4. FINALLY
# regardless whether there is an error or not, finally will be executed.

class SylviaError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    print("Let's divide numbers")
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    if num1 >=10 or num2 >= 10:
        raise SylviaError("Check what you've entered: {}, {}" .format(num1, num2))
    print("{} divided by {} is {}" .format(num1, num2, int(num1/num2)))
except ValueError:
    print("Please enter value less than 10")
except SylviaError as err:
    print("Let's try again!")
    print(err) 
finally:
    print("Thank you for using my calculator!")
    
  
