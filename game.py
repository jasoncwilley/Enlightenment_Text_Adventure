import collections
import player
import world
import items







def play():
#Print the Inroduction to the Game 
    print("""*************************************************************************************\nWelcome to Choice City--the gateway to Enlightenment.  The streets of Choice City are     filled what you would expect given the name, Choices.  These Choices as well as the       ability to learn from your expierences will be critical to the sucess of your journey.        \n*************************************************************************************
                   "The unexamined life is not worh living. --Socrates" 
                   ****************************************************""")
#Call world.create_tiles() to create rooms
    world.create_tiles()
#Define player and call the Player class 
    player = Player()
#Condition to keep loop running while Player is alive and not on the victory tile
    while player.is_alive() and not player.victory:
#Define the room varialbe whichis the (player.x, player.y)
        room = world.tile_at(player.x, player.y)
#Prints the Room/Tile information when Player enters room
        print(room.intro_text())
#Sets up the modify_player variable 
        room.modify_player(player)
#Condition to keep loop running while Player is alive and not on the victory tile
        if player.is_alive() and not player.victory:
#If player hp > 0 and not entered the VictoryTile room then choose_action will be called
            choose_action(room, player)
#Checks to see if player is_live is not true and prints statement, closes loop and ends when True
        elif not player.is_alive():
#Statement printed when is_alive is True this closes the loop and ends the game after it prints
            print("Your current adventure has come to an end.  Not all paths lead to the other side of the City but nonetheless they are all equally important.  You and only you can determine the sucess or failure of any endevor, each adventure is as unique as the adventurer themsel.  'It is in your moments of decision that your destiny is shaped'.-- Anthony Robbins."  )

#Defines the choose_action vaiale for room and player classes/objects
def choose_action(room, player):
#Sets action = None
    action = None
#Starts while loop for the choose_action variable
    while not action:
#Sets available_actions = the get_availble_actions defined in the room and player class/objects
        available_actions = get_available_actions(room, player)
#Prompts the user for input related to the action they wish to take
        action_input = input("\r\n""What do you choose to do:?")
#Sets action = to the action_input requested in previous statement
        action = available_actions.get(action_input)
#Conditional statment to to test the action variable is valid or not     
        if action:
#if the action user input is valid then pass action()
            action()
#if the action user input not defined  in action() then pass to the print statement below
        else:
#Print "Invalid Action" if the user input is not one defined in action()
            print("Invalid action!")

#Defines get_available_actions for the room and player class/objects


#Defines the available actions available each loop for the room and player classes
def get_available_actions(room, player):
#Sets actions = OrderedDic() to equal the OrderedDict function
    actions = OrderedDict()
#Prints the available actions and a quote related to actions
    print("\r\n Actions are the seed of fate; deeds grow into destiny. --Jean Nidetch""\r\n")
#Conditional statement to determine what actions are availbe to the player
    if player.inventory:
#Prints the players inventory if the user inputs "i"
#action_adder(actions, 'i', player.print_inventory, "Press i to look in Backpack"
#If they are in a room with an enemy  and the enemy is alive then print "a" "n" "s" "e" "w" "h"   
        if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
##If they are in a room with an enemy  and the enemy is alive then print "a" 
##Selecting "n" will move them North by performing y -1
            if world.tile_at(room.x, room.y - 1):
             action_adder(actions, 'n', player.move_north, "Press n to Go North")
#Selecting "s" will move them South by performing y + 1
        if world.tile_at(room.x, room.y + 1):
             action_adder(actions, 's', player.move_south, "Press s to Go South")
#Selecting 'e' will move the player right by performing x + 1
        if world.tile_at(room.x + 1, room.y):
             action_adder(actions, 'e', player.move_east, "Press e to Go East")
#Selecting "w will move the player left by performing y - 1
        if world.tile_at(room.x - 1, room.y):
             action_adder(actions, 'w', player.move_west, "Press w to Go West")
#Test to check if player is available to increase hp
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")
#if player has < 100 hp and has item in inventory then "h" will increase hp
    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


play()
