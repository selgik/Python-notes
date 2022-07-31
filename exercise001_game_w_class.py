# credit: Nado Coding's "Python Free Course (Basic)" YouTube
# mimicking text-based-game using class. This is exercies covering note009-note011.
# in original YouTube, instrcutor used StarCraft example. I'm using cats' name from Metalnam's YouTube

from random import *

class Nuri:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} has been created" .format(name))
        
    def move(self, direction):
        print("{}: moving toward {} direction. [Speed: {}]" \
        .format(self.name, direction, self.speed))
        
    def damaged(self, damage):
        print("{}: -{} HP tired" .format(self.name, damage))
        self.hp -= damage
        print("{}: current HP is {}" .format(self.name, self.hp))
        if self.hp <=0:
            print("{}: is sleeping" .format(self.name))
            
### How to write child class ver.1: traditional way(?)            
class Muni(Nuri):
    def __init__(self, name, hp, speed, damage):
        Nuri.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, direction):
        print("{}: approaching toward {} direction. [Using HP:{}]" \
                .format(self.name, direction, self.damage))
                
### How to write child class ver2.: can assign values direclty.               
class Kori(Muni):
    def __init__(self):
        Muni.__init__(self, "Kori", 500, 30, 5)
    
    def pakchim(self):
        if self.hp >10:
            self.hp -=10
            print("{}: is under pakchim [HP: -10]"\
            .format(self.name))
        else:
            print("{}: does not have enough HP to use pakchim"\
            .format(self.name))
            
### Setting two characteristics under class                     
class Dari(Muni):
    yemin_developed = False
    
    def __init__(self):
        Muni.__init__(self, "Dari", 500, 40, 20)
        self.yemin_mode = False
        
    def set_yemin_mode(self):
        if Dari.yemin_developed == False:
            return # do nothing
                   # if Dari.yemin_developed is True, then do below:
        if self.yemin_mode == False: 
            print("{}: turning into yemin mode" .format(self.name))
            self.damage *=2
            self.yemin_mode = True
        else:
            print("{}: turning off yemin mode" .format(self.name))
            self.damage /=2
            self.yemin_mode = False

### How to write class: does not have to assign member variables in __init__            
class Mange:
    def __init__(self, escape_speed):
        self.escape_speed = escape_speed
        
    def escape(self, name, direction):
        print("{}: escaping from {} direction. [Speed: {}]"\
            .format(name, direction, self.escape_speed))

### How to use method overriding:         
class Kachil(Muni, Mange):
    def __init__(self, name, hp, damage, escape_speed):
        Muni.__init__(self, name, hp, 0, damage)
        Mange.__init__(self, escape_speed)
        
    def move(self, direction):
        self.escape(self.name, direction) #use Magne class
        
class Reymond(Kachil):
    def __init__(self):
        Kachil.__init__(self, "Jeomnam", 500, 10, 60)
        self.hungry = False
    
    def hungry_mode(self):
        if self.hungry == True:
            print("{}: turning off hungry mode." .format(self.name))
            self.hungry = False
        else:
            print("{}: turning on hungry mode." .format(self.name))
            self.hungry = True
            
def game_start():
    print("[Notice] Nuri Game has started!")
    
def game_finish():
    print("[Notice] Nurine is tired, let's get them sleep!")

    
### Let's start game!
game_start()
n1 = Kori()
n2 = Dari()
n3 = Reymond()
n4 = Muni("Muni", 700, 30, 50)
n5 = Kachil("Kachil", 500, 40, 60)

#make as list, to manage cats easily.
nurine = []
nurine.append(n1)
nurine.append(n2)
nurine.append(n3)
nurine.append(n4)
nurine.append(n5)

#let's move cats
for cats in nurine:
    cats.move("Metalnam") 
    
Dari.yemin_developed = True
print("[Notice] Dari is about to turn to yemin mode")

# let's prepare to approach
# isinstance: Which class' instance is created object?
for cats in nurine:
    if isinstance(cats, Kori):  #ie. if n1, n2... is Kori class' instance, run pakchim method.
        cats.pakchim()
    if isinstance(cats, Dari):
        cats.set_yemin_mode()
    if isinstance(cats, Reymond):
        cats.hungry_mode()
    
# attack
for cats in nurine:
    cats.attack("Metalnam's garden")
    
# damaged
for cats in nurine:
    cats.damaged(randint(5,21))
    
game_finish()

### result:
# [Notice] Nuri Game has started!
# Kori has been created
# Dari has been created
# Jeomnam has been created
# Muni has been created
# Kachil has been created
# Kori: moving toward Metalnam direction. [Speed: 30]
# Dari: moving toward Metalnam direction. [Speed: 40]
# Jeomnam: escaping from Metalnam direction. [Speed: 60]
# Muni: moving toward Metalnam direction. [Speed: 30]
# Kachil: escaping from Metalnam direction. [Speed: 60]
# [Notice] Dari is under yemin mode
# Kori: is under pakchim [HP: -10]
# Dari: turning into yemin mode
# Jeomnam: turning on hungry mode.
# Kori: approaching toward Metalnam's garden direction. [Using HP:5]
# Dari: approaching toward Metalnam's garden direction. [Using HP:40]
# Jeomnam: approaching toward Metalnam's garden direction. [Using HP:10]
# Muni: approaching toward Metalnam's garden direction. [Using HP:50]
# Kachil: approaching toward Metalnam's garden direction. [Using HP:40]
# Kori: -17 HP tired
# Kori: current HP is 473
# Dari: -19 HP tired
# Dari: current HP is 481
# Jeomnam: -9 HP tired
# Jeomnam: current HP is 491
# Muni: -7 HP tired
# Muni: current HP is 693
# Kachil: -20 HP tired
# Kachil: current HP is 480
# [Notice] Nurine is tired, let's get them sleep!
