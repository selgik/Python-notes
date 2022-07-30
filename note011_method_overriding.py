#note011_method_overriding.py

########## 1. OPERATOR OVERLOADING
#1) Let's see below codes:
#   Similar to previous codes (from note010 but added new member variable (speed) and def move().

class Unit:   
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
   
    def move(self, location):
        print("[Ground unit is moving]"
        print("{} is moving toward {} direction. [Speed: {}]"\
              .format(self.name, location, self.speed))
        
class AttackUnit(Unit):   
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   
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
      
 class Fly_Unit:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(sef, name, location):
        print("{}: Flying toward {} direction. [Flying speed: {}]" \
              .format(name, location, self.flying_speed)) 

  class Fly_AttackUnit(AttackUnit, Fly_Unit): 
    def __init__(self, name, hp, damage, flaying_speed):
      AttackUnit.__init__(self, name, hp, 0, damage)
      Fly_Unit.__init__(self, fying_speed)

#in this scenario, if we want to create two units - one for ground unit and another one for air unit, we need to create as:
vulture = AttackUnit("Virture", 80, 15, 20)
battlecruiser = Fly_AttackUnit("Battlecruiser", 500, 20, 10)
vulture.move("11 o'clock")
battlecruiser.fly(battlecruiser.name, "10 o'clock")

#problem is: we need to use move() or fly() depending on whether unit is ground or air one. 
#solution: using method overriding, we can use one function and make both unit move/fly.
#how to: add one more function under class Fly_AttackUnit :

#2) Method overriding
              
    class Fly_AttackUnit(AttackUnit, Fly_Unit): 
        def __init__(self, name, hp, damage, flaying_speed):
          AttackUnit.__init__(self, name, hp, 0, damage)
          Fly_Unit.__init__(self, fying_speed)   
              
        def move(self, location):
          print("[Air unit is moving]")
          self.fly(self.name, location)
              
 #let's then test out:
  vulture = AttackUnit("Virture", 80, 15, 20)
  battlecruiser = Fly_AttackUnit("Battlecruiser", 500, 20, 10)
  vulture.move("11 o'clock")
  battlecruiser.move("10 o'clock")             

 #result: 
 # [Ground unit is moving]
 # Virture is moving toward 11 o'clock direction. [Speed: 15]
 # [Air unit is moving]
 # Battlecruiser : Flying toward 10 o'clock direction. [Flying speed: 10]"
              
              
