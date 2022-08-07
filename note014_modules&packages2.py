#note014_modules&packages2.py

########## 1. INSTALL PACKAGES
# google keyword pypi and you will find https://pypi.org which is python package index.
# we can search package that has been created and verified by others.
# ex. beautifulsoup 

# 1) how to install packages:
# enter below to the PowerShell
pip install beautifulsoup4

# 2) let's test out using codes under Quick Start in pypi.org search page:
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 3) enter below to the PowerShell to see which package/versions have been installed:
pip list

# 4) check the information about the package by entering below to the PowerShell:
pip show beatifulsoup4

# 5) to update:
pip install --upgrade beautifulsoup4

# 6) remove:
pip uninstall beautifulsoup4


########## 2. BUILT-IN FUNCTIONS
# 1) google search 'list of python builtins' you will see built-in functions documentation.
# 2) input is an example of Python built-in function. 
# 3) another one is dir will return all properties and methods of the specified object.

print(dir())        #you will see the list of properties/method
import random
print(dir())        #you will see 'random' is added
import pickle
print(dir())        #you will see 'pickel' is added next to 'random'

# what can I do with random?
import random
print(dir(random))  #you will see familiar functions such as shuffle or randrange.

# what can I do with list?
list = [1, 2, 3]
print(dir(list))    #you will see lot of items including append, clar, copy etc.

# and with variable?
var = "Jim"
print(dir(var))     #you will see lot of items including lower, isalpha etc.


########## 3. PYTHON MODUELS (TO BE USED WITH IMPORT)
# 1) google search 'list of python modules' and check the index.
# 2) example of python module: random
# 3) another one is glob, which checks the folder/file's path 

import glob
print(glob.glob("*.py")     
#result: will list the file that has extension .py 

# 4) os: show current directory
import os
print(os.getcwd())
#result: current path (ex. C:\Users\Sylvia\Desktop\Python_Worksplace

# using os, let's create a folder if there is no such one. If there is one, remove it.
import os
folder = "sample_folder"
if os.path.exists(folder):
      print("folder already existing")
      os.rmdir(foldr) #if exists, remove folder
      print(folder, "folder has been removed")
else:
      os.makedirs(folder)
      print(folder, "folder has been created")

# similar to dir, let check what os can do:
import os
print(os.listdir())
  
# 5) time related function
import time
print(time.localtime())                           #result won't be user-friendly to read
print(time.strftime("%Y-%m-%d %H:%M:%S"))         #result: 2022-08-07 06:38:22 *** Make sure to use this form ***
print(time.strftime("%y-%m-%d %h:%m:%s"))         #result: 22-08-07 Aug:08:1659854321
print(time.strftime("%Y-%M-%D %H:%M:%S"))         #result: 2022-38-08/07/22 06:38:41
      
# 6) datetime
import datetime
print("today's date is", datetime.date.today())   #result: today's date is 2022-08-07

# 7) datetime - timedelta (difference between times)
import datetime
today = datetime.date.today()
anniversary = datetime.timedelta(days=100)
print("our anniversary is", today+anniversary)    #result: our anniversary is 2022-11-15
      
      
