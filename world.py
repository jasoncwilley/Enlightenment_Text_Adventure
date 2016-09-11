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
**************************************************************************** 
* Welcome to Choice City--the gateway to Enlightenment.  The streets of    *
* Choice *City are filled what you would expect given the name, Choices.   *
* These Choices as well as the ability to learn from your expierences will *
* be critical to the sucess of your journey.                               *  
****************************************************************************
                            
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
***********************************************************************
*  Out of nowhere you find yourself surrounded by a pack of vicious   *
*  hater wolves.  These wolf like creatures feast on insecurities and *
*  would like nothing more than to eviscerate your selfconfidence.    *
***********************************************************************

****************************************************************** 
**"Dout will kills more dreams than failure ever will." --Kassem** 
******************************************************************
"""
            self.dead_text =  """
********************************************************************   
* The wolves proved to be stronger than you thought.  You were     * 
* not able to reach the the Magical Forest on the other side of    *
* the City.  Learning from  your mistakes will put your on the     *
* fast track to Enlightenment and if you can apply thesel lessons  *
* in your next life you be more likely to suceed.                  *
********************************************************************

***************************************************************
**"Doubt kills more dreams than failure ever will." --Kassem **
***************************************************************
"""

#if e ia < .0.75 hen select Ogre for the user to face and .alive_text
        elif r < 0.75:
#if r is lessthank            
            self.enemy = enemies.Ogre()
            self.alive_text = """
**************************************************************************
* An ogre sized ego is blocking your path!Egos that have grown to the    *  
* size of this the Ogre's can do only one thing! Well 2 things, to be    * 
* correct all the time and keeping you from achieving enlightment        *
* Learning to apologize does not mean you are wrong and another person   *
* is right. Respecting other's beliefs even when they go against your    * 
* own may not easy but Hey!, Do you want to be right or happy? The       *
* choice is yours.                                                       *
**************************************************************************
"""
            self.dead_text= """ 
*************************************************************************
*   Wow! You were able to check that ogre's ego with tact and class.    *
*  Choices like that will surely lead you to the other side of the City.* 
*************************************************************************

********************************************************************
* The Ancients say 'Yeild to overcome; Bend and be straight;       *    
* Empty and be full; Wear out to become new; Have little and gain; *
* Have much and be confused...                                     *
******************************************************************** 
"""
                               
        elif r < 0.85:
            self.enemy = enemies.KarmaChameleon()
            self.alive_text = """
***********************************************************************
* You feel the wind pick up and you are suddenly lost in swarm of     *
* bommerangs!  You quickly notice that these are not your average     *  
* everyday boomerangs but instead one's that you threw in the         * 
* distant past.  Everyone has a past or a history of Choices and      *
* if this has happend to you while on your journey through the city   *
* take a breath and deal with your karma now because by it's very     *
* nature it's not coming back to or for you.  Hopefully the former!   *
***********************************************************************
"""

            self.dead_text =  """                                                         
************************************************************************** 
* Dozens of boomerangs have hit your and knocked you to the ground.      *
* Look on the bright side you were able to settle an recent or age old   * 
* karmatic debt.                                                         *
**************************************************************************  
**********************************************************
*  "There is such thing as good or bad, right or wrong,  *
*    those are perspectives of what actual is" --Tolle   * 
**********************************************************
"""                              

        else:
           self.enemy = enemies.KarmaChameleon()
           self.alive_text = """                                                                                                                                                   
*********************************************************************
* You feel the wind pick up and you are suddenlylost in swarm of    *
* bommerangs! You quickly notice that these are not your average    *
* everyday boomerangs but instead one's that you threw in the       *    
* distant past.  Everyone has a past or a history of Choices and    *   
* if this has happend to you while on your journeythrough the city  *
* take a breath and deal with your karma now because by  it's very  *
* nature it's not coming back to or for you. Hopefully the former!  *
*********************************************************************
"""


           self.dead_text =  """
*********************************************************************
* Dozens of boomerangs have hit your and knocked you to the ground. * 
* Look on the bright side you were able to settle an recent or age  *
* old karmatic debt.                                                *
*********************************************************************

******************************************************************
*"There is such thing as good or bad, right or wrong, those are  * 
* perspectives of what actual is' --Tolle                        * 
******************************************************************
"""
        super().__init__(x, y) #Defines the intro_text Player will see when they enter room

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))


class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
****************************************************************************
* As you approach the far end of the City you stop to gather your          *
* thoughts and appreciate the moment.  As you turn down the road labeled   *
* Destiny Lane you see a structure a beautiful palace in the distance.     *
* Excited youwalk faster and begin to run.  Enlightment is in your site    *
* and youare determinded to get there before night fall.  As the sun goes  *
* downyou keep walking towards the mystical destination.  Late into the    *  
* night you are exhuausted and have to stop to sleep.You tell yourself     *
* It has to be close.  When the sun rises you jump up and quickly notice   *
* that you are not any closer to the destination than you were the day     *
* before.  At this point you decide to turn around because the realization *
* that Enlightment is a process not a destination.  How far you go down    *
* Destiny Lane is exactly how fare you go down Destiny Lane, if you even   *
* make it there, depends on you.                                           *
****************************************************************************

**********************************************
* Victory Is Yours! or Maybe This is Defeat? *
*   Like everything else the Choice is Yours!*
**********************************************
"""


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
*****************************************************
* The alley you choose to go down is quiet and dark *
* You forge onwards.                                *
*****************************************************
"""
        else:
            return """
*******************************************************
* Your good Karma is paying off, literally.  You find *
* some gold on the ground                             *
*******************************************************            
"""

#
#class TraderTile(MapTile):
#    def __init__(self, x, y):
#        self.trader = npc.Trader()
#       super().__init__(x, y)

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
*******************************************************
*  Out of the corner of you eye you see a purse full  * 
*  of gold.  Your inner guide senses danger so you    *      
*  decide to ignore it and forge on.                  *
*******************************************************
"""

world_dsl = """
|EN|EN|VT|EN|EN|
|FG|  |EN|  |EN|
|FG|FG|EN|  |FG|
|FG|  |ST|FG|EN|
|FG|  |EN|  |FG|
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
#                  "TT": TraderTile,
                  "  ": None}


world_map = []

start_tile_location = None


def parse_world_dsl():
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
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
