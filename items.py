class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
    
    def __str__(self):
        return self.name

class Kindness(Weapon):
    def __init__(self):
        self.name = "Kindness"
        self.description = "Kindness can never be underestimated. "
        self.damage = 25
        self.capacity = 16

class Meditation(Weapon):
    def __init__(self):
        self.name = "Meditation"
        self.description = "When in doubt Meditation can prove to be a powerful weapon. "
        self.damage = 25
        self.capacity = 1

class Forgiveness(Weapon):
     def __init__(self):
        self.name = "Forgiveness"
        self.description = "Forgiveness is the key to every door. "
        self.damage = 15
        self.capacity = 8
	
class Consumable:
    def __init__(self):
        def __str__(self):
           return "{} (+{} HP)".format(self.name, self.healing_value)

class BeefJerky(Consumable):
   def __init__(self):
        self.name = "BeefJerky"
        self.healing_value = 15
        self.value = 12    
class HealingPtion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 25