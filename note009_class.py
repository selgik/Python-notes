#note009_class.py

########## 1. WHY WE NEED A CLASS
# Let's think about this scenario. You are creating a game, StarCraft. 
# You first create a Marine and then a tank.

name = "Marine"
hp = 40
damage = 5
print("{} unit has been created." .format(name))
print"HP is {} and damage is {}.\n" .format(hp, damage))

t_name = "Tank"
t_hp = 150
t_damage = 35
print("{} unit has been created." .format(name))
print"HP is {} and damage is {}.\n" .format(hp, damage))

def attack(name, location, damage):
  print("{}: attacking toward {} direction. [Damage: {}]\n" .format(name, location, damage))

attack(name, "1 o'clock", damage)
attack(t_name, "3 o'clock", t_damage)

#Result:
#Marine unit has been created.
#HP is 40 and damage is 5.
#Tank unit has been created.
#HP is 150 and damage is 35.
#Marine: attacking toward 1 o'clock direction. [Damage: 5]
#Tank: attacking toward 3 o'clock direction. [Damage: 35]

#But:
#what if we need to create second tank? third and forth etc? 
#We might be able to add few but in real game, we need 10+ or 100+ units.
#Think about waffle tool. We just need tool to generate units easily. We need here CLASS.


########## 2. WHAT IS A CLASS
#1) class contains group of related variales and functions.

class Unit:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{} unit has been created." .format(self.name))
    print("HP is {}, damage power is {}." .format(self.hp, self.damage))
    
marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank1 = Unit("Tank", 150, 35)
wrath1 = Unit("Wrath", 150, 35)

# __init__ : creator
# marine, tank: a. created from class. They are called OBJECTS. 
#                  in order to create OBJECTS, need to input same data as declared (ie. name/hp/damage).
#               b. they are Unit class' INSTANCE.          
# name/hp/damage: they are member variables. They are defined within the class and we can reset/use them.

# 2) how to access to member variable from outside the class? See below:

print("Unit name is {}, hp is {} and damage power is {}." .format(wrath1.name, wrath1.hp, wrath1.damage)

# 3) can I assign variable from outside class too? See below:

wrath2 = Unit("Wrath_new", 150, 35)
wrath2.clocking = True
if wrath2.clocking == True:
      print("{} is under clocking." .format(wrath2.name))

#result is: Wrath_new is under clocking.
#but below will give errors because we've only assigned clocking to wrath2.
#clocking variable is NOT within the class. It is outside the class.

wrath2.clocking = True
if wrath1.clocking == True:
      print("{} is under clocking." .format(wrath2.name))
      

########## 3. METHOD

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
  
    #method1: attack
    def attack(self, location):
      print("{}: attacking toward {} direction. [Damage: {}]"\
            .format(self.name, location, self.damage))
   
    #method2: damaged
    def damaged(self, damage):
      print("{}: {} damaged." .format(self.name, damage))
      self.hp -= damage
      print("{}: current hp is {}." .format(self.name, self.hp))
      if self.hp <=0:
        print("{}: unit has been destroyed" .format(self.name))
      
firebat1 = AttackUnit("Firebat", 50, 15)
firebat1.attack("5 o'clock")
firebat1.damaged(25)      
firebat1.damaged(25)
      
#Result:      
#Firebat: attacking toward 5 o'clock direction. [Damage: 15]
#Firebat: 25 damaged.
#Firebat: current hp is 25
#Firebat: 25 damaged.
#Firebat: current hp is 0
#Firebat: unit has been destroyed
      
      
