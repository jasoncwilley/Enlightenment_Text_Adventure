import enemies
import random


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

#Defines StartTile as an object in the MapTile class 
class StartTile(MapTile):
#Defines the introduction text that will player will see when they are on the StartTile 
    def intro_text(self):
# Text below will populate the StartTile variable intro-text
        return """
*************************************************************************************\n
Welcome to Choice City--the gateway to Enlightenment.  The streets of Choice City are     
filled what you would expect given the name, Choices.  These Choices as well as the       
ability to learn from your expierences will be critical to the sucess of your journey.
*************************************************************************************
                                   

      *******************************************************************
      ********"The unexamined life is not worh living." --Socrates*******
      *******************************************************************
"""

#creates and inits the EnemyTile Object in the MapTile Class
class EnemyTile(MapTile):
#defines aand inits self, x and y for the EnemyTile object   
    def __init__(self, x, y):
#sets r = random in the random module
        r = random.random()
#if r < less than 0.50 then select Wolves for the user to face
        if r < 0.50:
        
            self.enemy = enemies.Wolves()
# sets .alive_text             
            self.alive_text = """
********************************************************************************************
Out of nowhere you find yourself surrounded by a pack of vicious hater wolves.  These wolf 
like creatures feast on insecurities and would like nothing more than to eviscerate your 
self-confidence. *******************************************************
                *Not Today!  Your Attack seems to be working. Nice move!*
                 *******************************************************                     
             ****************************************************************                 
           **"Dout will kills more dreams than failure ever will." --Kassem**
********************************************************************************************"""
            self.dead_text = """The wolves proved to be stronger than you thought.  You were 
not able to reach the the Magical Forest on the other side of the City.  Learning from your 
mistakes will put your on the fast track to Enlightenment and if you can apply thesel lessons
in your next life you be more likely to suceed.                                               
********************************************************************************************S
              **"Dout will kills more dreams than failure ever will." --Kassem**
********************************************************************************************"""

#if e ia < .0.75 hen select Ogre for the user to face and .alive_text
        elif r < 0.75:
#if r is lessthank            
            self.enemy = enemies.Ogre()
            self.alive_text = """
*********************************************************************************************
An ogre sized ego is blocking your path!Egos that have grown to the ize of this the Ogre's 
can do only one thing! Well 2 things, to be correct all the time and keeping you from 
achieving enlightment Learning to apologize does not mean you are wrong and another person 
is right. Respecting other's beliefs even when they go against your own may not easy but hey!, 
Do you want to be right or happy? The choice is yours.
*********************************************************************************************"""

            self.dead_text=  "Wow! You were able to check that ogre's ego with tact and class. Choices like that will surely lead you to the other side of the City."\
                              "The Ancients say 'Yeild to overcome; Bend and be straight; Empty and be full;"\
                              "Wear out to become new; Have little and gain; Have much and be confused...'" 
                               
        elif r < 0.85:
            self.enemy = enemies.KarmaChameleon()
            self.alive_text = """
You feel the wind pick up and you are suddenlylost in swarm of bommerangs!  You quickly notice that these are not your average everyday boomerangs but instead one's that you threw in the distant past.  Everyone has a past or
or a history of Choices and if this has happend to you while on your journey through the city take a breath and deal with your karma now because by it's very nature it's not coming back to or for you.  Hopefully the former!" 
self.dead_text =  Dozens of boomerangs have hit your and knocked you to the ground.  Look on the bright side you were able to settle an recent or age old karmatic debt. 'There is such thing as good or bad, right or wrong, those are perspectives of
what actual is' --Tolle 
"""                              
        else:
            self.enemy = enemies.KarmaChameleon()
            self.alive_text = """
You feel the wind pick up and you are suddenlylost in swarm of bommerangs!  You quickly notice that these are not your average everyday boomerangs but instead one's that you threw in the distant past.  Everyone has a past or
or a history of Choices and if this has happend to you while on your journey through the city take a breath and deal with your karma now because by it's very nature it's not coming back to or for you.  Hopefully the former!" 
self.dead_text =  Dozens of boomerangs have hit your and knocked you to the ground.  Look on the bright side you were able to settle an recent or age old karmatic debt. 'There is such thing as good or bad, right or wrong, those are perspectives of
what actual is' --Tolle """
        super().__init__(x, y)
#Defines the intro_text Player will see when they enter room
    def intro_text(self):
#Conditions to determine which text Player will see when they enter room 
#if they checks to see if player is alive
#if so, then to see if enemy is alive
#else it will print the dead_text variable
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
#returns one of the three variables listed above depeding on stated conditions
        return text



#Defines conditions to modify the player's attributes if...
    def modify_player(self, player):
        #Condition to test if enemy is alive enemy.hp > 0
        if self.enemy.is_alive():
            #Determins the amount of damage enemy will inflict on player
            player.hp = player.hp - self.enemy.damage
            #Reports damage done by enemy and player's remaining HP
            print("Enemy does {} damage. You have {} HP remaining.".
                  #defines which variables will be used in the previous statement
                  format(self.enemy.damage, player.hp))

#Defines the VictoryTile Object of the MapTile Class
class VictoryTile(MapTile):
#Determines if the player is victorytile or not and adjust play.victory variable from Fals to True
    def modify_player(self, player):
        #sets player.victory to True this will close the game loop and end the game
        player.victory = True

    def intro_text(self):""
"""***************************************************************************************************************************\n
As you approach the backside of the City you stop to gather your thoughts and appreciate the moment.  You turn            *\n
down the road labeled Destiny lane and see the a structure in the distance.  Excited you walk faster and begin            *\n
to run.  Enlightment is in your site and you are determinded to get there before night fall.  As the sun goes down        *\n
you keep walking towards the mystical destination.  Late into the night you are exhuausted and have to stop to sleep.     *\n
You tell yourself "It has to be close"  When the sun rises you jump up and quickly notice that you are not any closer     *\n
to the destination than you were the day before.  At this point you decide to turn around because the realization that    *\n
Enlightment is a process not a destination.  How far you go down Destiny Lane is exactly how fare you go down Destiny     *\n
Lane, i  f you even make it there, depends on you.                                                                        *\n
***************************************************************************************************************************\n
                             * ********************************************
                             * Victory Is Yours! or Maybe This is Defeat? *
                             *   Like everything else the Choice is Yours!*
                             **********************************************"""
       
#Defines and inits the FindGoldTile object in the MapTile class
class FindGoldTile(MapTile):
#inits self and x, y    
    #super inits x and y        
    def __init__(self, x, y):
        super().__init__(x, y)
#sets gold for Karma Tiles between 1 and 85 randomly                
        self.gold = 10
#sets gold_claimed to false        
        self.gold_claimed = False
    def modify_player(self, player):
        if not self.gold_claimed:
               self.gold_claimed = True
               self.gold = player.gold + self.gold
        print("+{} gold added.".format(self.gold))
        
# dedines intro_text for to be 
    def intro_text(self):
    #sers up condition to print the text depending on gold_claimed         
        if self.gold_claimed:
           return """
                The streets are unusually quiet...
                """
        else:
          return """
                Someone dropped some gold. You pick it up.
                """

#Defines Grid for world map (x,y)
#(0,0) (0,1) (0,2) (0,3) (0,4) (0,5)
#(1,0) (1,1) (1,2) (1,3) (1,4) (1,5)
#(2,0) (2,1) (2,2) (2,3) (2,4) (2,5)
#(3,0) (3,1) (3,2) (3,3) (3,4) (3,5)
#(4,0) (4,1) (4,2) (4,3) (4,4) (4,5)
#(5,0) (5,1) (5,2) (5,3) (5,4) (5,5)

world_dsl = """
|EN|EN|EN|EN|EN|
|VT|  |  |  |EN|
|EN|FG|EN|  |FG|
|FG|  |ST|FG|EN|
|FG|  |EN|  |FG|
"""
class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def intro_text(self):
        return """
       Describe the Trading Post...
        """
def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "  ": None}


world_map = []

start_tile_location = None
#world fuction that creates a function to create the rooms/map for the game.
def create_tiles():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) 
                if tile_type else None)

        world_map.append(row)




def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
