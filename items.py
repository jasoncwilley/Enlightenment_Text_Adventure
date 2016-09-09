#Creates Weapon class
class Weapon:
# inits wealpon class
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
#defines the .name object/method as a string variable
    def __str__(self):
#returns te name of the Weapon.name variable
        return self.name
#Kindness Object
class Kindness(Weapon):
#Inits and defines the Kindness object from the weapon class
    def __init__(self):
#defines name of kindess weapon class to kindness
        self.name = "Kindness"
#defines desscripton of of the kindness object of the weapon class
        self.description = "Kindness can never be underestimated. "
#set's the damage that kindness will inflict on the enemy each 
        self.damage = 25

#Inits and defines the Meditation object as well as the damage it does to the enemy
class Meditation(Weapon):
    def __init__(self):
        self.name = "Meditation"
        self.description = "When in doubt Meditation can prove to be a powerful weapon. "
        self.damage = 15

#Inits and defines the Forgiveness object as well as the damage it does to the enemy
class Forgiveness(Weapon):
     def __init__(self):
        self.name = "Forgiveness"
        self.description = "Forgiveness is the key to every door. "
        self.damage = 30

#Creates and inits the consumable class
class Consumable:
    def __init__(self):
        
#returns the name and the heal vaule of of thd consumable        
        return "{} (+{} HP)".format(self.name, self.healing_value)
#creates and inits the beefjerky in the consumable class with name and healing value
class BeefJerky(Consumable):
   def __init__(self):
        self.name = "BeefJerky"
        self.healing_value = 20

