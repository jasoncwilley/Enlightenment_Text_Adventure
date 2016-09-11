#Weapon
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
    def __str__(self):
        return self.name
#Kindness Object
class Kindness(Weapon):
    def __init__(self):
        self.name = "Kindness"
        self.description = "Kindness can never be underestimated. "
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
        raise NotImplementedError("Do not create raw Consumable objects.")   
    def __str__(self):          
        return "{} (+{} HP)".format(self.name, self.healing_value)

#Creates and inits the beefjerky in the consumable class with name and healing value
class BeefJerky(Consumable):
    def __init__(self):
        self.name = "Beef Jerky"
        self.healing_value = 20
        self.value = 15
#Creates Healing Potion adn set's it's value to 50 and healing value to 50
class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 50
