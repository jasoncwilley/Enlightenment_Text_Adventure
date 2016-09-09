class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Wolves(Enemy):
    def __init__(self):
        self.name = "Wolves of Self Doubt"
        self.hp = 20
        self.damage = 10

class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre the Ego"
        self.hp = 60
        self.damage = 15

class KarmaChameleon(Enemy):
    def __init__(self):
        self.name = "Karma Chameleon"
        self.hp = 100
        self.damage = 12
    
