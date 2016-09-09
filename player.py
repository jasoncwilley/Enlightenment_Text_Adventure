
import items
import world
import player
import random
#Creates and inits the Player Class 
class Player:
    def __init__(self):
#identifies the inventory varialbes         
        self.inventory = [items.Kindness(), items.Forgiveness(), items.Meditation(), items.BeefJerky()]
#defines the statting cordinates with x any        
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
#defines playing stating health value
        self.hp = 100
#defines amount of gold you start with
        self.gold = 5
#Condition stating the Player has not won the game
        self.victory = False

#Creates is_alive to test if Health is > 0 F
    def is_alive(self):
        return self.hp > 0
#defines print_inventory as item in inventory 
    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
#prints items in the invetory
            print('* ' + str(item))
#prints the amount od gold player has
            print("Gold: {}".format(self.gold))

# defines the healing items in inventory
    def heal(self):
        consumables = [item for item in self.inventory

        if isinstance(item, items.Consumable)]
#if you don't have consumables prints the statement  
        if not consumables:
            print("You don't have any items to heal you!")
            return

#if you have consumable items  this prints the amount nd item
        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))
#whn not valid the players is asked to chooos which consumable to us
        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
#sets the hp and removes the item from the inventory once used               
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
#calulates new hp value and reports it                
                print("Current HP: {}".format(self.hp))
#sets conditions to print invalid option to print                 
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = best_weapon.name
        best_weapon.name = Meditation
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

#defines attack function by determining the best weapon and sets enemy to room.enemy
    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
#prints what weapon is used againt the enemy name        Sprint("You use {} against {}!".format(enemy.hp enemy.name))
#determins the amount of damage is inflicted on enemy and test if they are still alive throug is_alive if 
#false prints you defeated the enenmy or  the enemy's name and thier new hp
    #enemy.hp -= best_weapon.damage
#    print("You killed {}!".format(enemy.name))
   # else:
    #        print("{} HP is {}.".format(enemy.name, enemy.hp))

