#note009_class.py

########## 1. INHERITANCE
#1) From previous codes, let's see if I can create a Medic. 
# Medic cannot attack, so from AttackUnit, 'damage(power)' should be removed. 

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
# so I would be to create new class like below:

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# Hold on, there is similarity between class AttackUnit and class Unit. 
# Let's use inheritance. 

#2) I will assign Unit class as parent class and AttackUnit as child class. 

class Unit:   
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
class AttackUnit(Unit):   #AttackUnit is inheriting from Unit class
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   #This is how inheritance works
        self.damage = damage

    def attack(self, location):
        print("{}: attacking toward {} direction. [Damage: {}]" \
              .format(self.name, location, self.damage))
        
    def damaged(self,damage):
        print("{}: {}damaged" .format(self.name, damage))
        self.hp -=damage
        print("{}: current hp is {}" .format(self.name, self.hp))
        if self.hp <=0:
          print("{}: Unit has been destroyed." .format(self.name))
 
firebat = AttackUnit("Firebat", 30, 18)


########## 2. MULTIPLE INHERITANCE
#1) Multiple inheritance: if we have many parent classes that can inherit to child class
#   Let's try to create a dropship (aircraft unit / they cannot attack)
#   First, we will still have both classes for Unit and AttachUnit

class AttackUnit(Unit):   #AttackUnit is inheriting from Unit class
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   #This is how inheritance works
        self.damage = damage

    def attack(self, location):
        print("{}: attacking toward {} direction. [Damage: {}]" \
              .format(self.name, location, self.damage))
        
    def damaged(self,damage):
        print("{}: {}damaged" .format(self.name, damage))
        self.hp -=damage
        print("{}: current hp is {}" .format(self.name, self.hp))
        if self.hp <=0:
          print("{}: Unit has been destroyed." .format(self.name))
 
 #2) Let's create new class for dropship:       
 class Fly_Unit:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(sef, name, location):
        print("{}: Flying toward {} direction. [Flying speed: {}]" \
              .format(name, location, self.flying_speed)) 
              #it is not self.name because in class Flyable, we do not have inherited name

 #3) Let's create new class for Valkyrie (aircraft that can attack) using multiple inheritance:
  class Fly_AttackUnit(AttackUnit, Fly_Unit): #inheriting from both classes
    def __init__(self, name, hp, damage, flaying_speed):
      AttackUnit.__init__(self, name, hp, damage)
      Fly_Unit.__init__(self, fying_speed)
      
 # Let's test out!
  valkyrie = Fly_AttackUnit("Valkyrie", 200, 15, 5)
  valkyrie.fly("Valkyrie", "2 o'clock")
  
 #result: 
 #Valkyrie: Flying toward 2 o'clock direction. [Flying speed: 5]
        

########## 3. SUPER
#1) Let's create class Building inheriting from class Unit:
class Building(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self, name, hp)
        self.location = location
        
# Using super, Unit.__init part can be changed as below:
class Building(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp) 
        self.location = location
        
# when using super, there is no need to add 'self'.
# but problem will appear if super is used for multiple inheritance cases.

#2) Using super in multiple inheritance:
# let's simplify the example scenario.

class First:
    def __init__(self):
        print("First printed")
        
class Second:
    def __init__(self):
        print("Second printed")
        
class Test(First, Second):
    def __init__(self):
        super().__init__()

temp = Test()

# result: First printed.
#         If we change order as class Test(Second, First), result will be "Second printed".
# When using super, function from the first parent class will be called. 
# Therefore, when using super we need to make sure to use traditional multiple inheritance codes, like below:

class First:
    def __init__(self):
        print("First printed")
        
class Second:
    def __init__(self):
        print("Second printed")
        
class Test(First, Second):
    def __init__(self):
        Fist.__init__(self)
        Second.__init__(self)

temp = Test()

#result: First printed Second printed
