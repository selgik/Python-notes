#note013_modules.py

########## 1. MODULES
# modules: file containing a set of functions (file that holds all parts). Modules in python has extension of .py
# in order to use modules: a. module file needs to be in the same path (ex. python_workspace
#                          b. or in the same folder where python libraries are.

# 1) Let's create modules to see how it works. 
# create a theatre_module.py file and add below codes:

def price(people):
  print("Normal price for {} people are: {}" .format(people, people*100))
  
def morning_price(people):
  print("Morning price for {} people are: {}" .format(people, people*60))

def special_price(people):
  print("Special price for {} people are: {}" .format(people, people*40))
  
# 2) Let's say you are currently in the practice.py module.
# 2-1) import. (remark: I should run theatre_module.py first before using them)
import theatre_module
theatre_module.price(3)
theatre_module.morning_price(3)
theatre_module.special_price(3)

# 2-2) from module import *
from theatre_module import *
price(3)
morning_price(3)
special_price(3)

# 2-3) from module import selectively
from theatre_module import price, morning_price
price(3)
morning_price(3)
special_price(3) #this will give an error!


########## 2. NAMING THE MODULE (ALIS)
# 1) alias module
import theatre_module as tm
tm.price(3)
tm.morning_price(3)
tm.special_price(3)

#2) alias function
from theatre_module import special_price as price
price(3) #this is not the same price() in the origianl theatre_module!


########## 3. PACKAGES
# packages: group of modules
# in order to use packages: a. create folder (ex. travel)
#                           b. under travel, create modules (ex. thailand.py, vietnam.py, __init__.py)

# 1) let's create basic class for both thailand.py and vietname.py
# under thailand.py:
class ThailandPackage():
  def detail(self):
    print("[Thai Package] BKK, Pataya: 5K USD")
   
# under vietnam.py:    
class VietnamPackage():
   def detail(self):
    print("[Viet Package] Danang: 2K USD") 
    
# under __init__.py:    
# leave it empty for now

# 2) Let's say you are currently in the practice.py module and want to use travel package.
# 2-1) import 
import travel.thailand #here we can only import module or packages, not class or function.
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
# result: [Thai Package] BKK, Pataya: 5K USD

#2-2) from module import 
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()
# result: [Thai Package] BKK, Pataya: 5K USD

#2-3) from package folder import module
from travel import vietnam
trip_to = vietnam.VietPackage()
trip_to.detail()
# result: [Viet Package] Danang: 2K USD


########## 3. __init__.py
# 1) __all__ = [""]

# if we try as below, we will receive an error message that vietnam is not defined. 
from travel import *
trip_to = VietnamPackage()
trip_to.detail()

# we need to update __init__.py file as below so that above codes work:
__all__ = ["vietnam"]

# Below won't work out because vietnam is open/shared as per above, but not thailand.
from travel import *
trip_to = ThailandPackage()
trip_to.detail()

# need to update __init__.py file again to use above:
__all__ = ["vietnam", "thailand"]

# 2) Executed within the module or outside of module?
# let's update travel.thailand.py 

class ThailandPackage():
  def detail(self):
    print("[Thai Package] BKK, Pataya: 5K USD")
   
if __name__ == "__main__":
  print("printing this message because function is being run inside the thailand module")
  trip_to = ThailandPackage()
  trip_to.detail()
else:
  print("function is being run outside the thailand module")
  
# now let's try both a. run function within thailand module and outside(ex. practice.py) as below:
from travel import *
trip_to =  ThailandPackage()
trip_to.detail()
# result: function is being run outside the thailand module 
#         [Thai Package] BKK, Pataya: 5K USD


########## 4. PACKAGE AND MODULE'S LOCATION
# 1) How to check location of package?
import inspect
import random
print(inspect.getfile(random))
# result: C:\Python310\lib\random.py

# another example:
import inspect
from travel import *
print(inspect.getfile(thailand))
# result: c:\Users\Sylvia\Desktop\Python_Workspace\travel\thailand.py

#2) Why is it important? What is it for?
# By knowing the location, you can copy/paste/move modules to use for your own project. 
    
 
