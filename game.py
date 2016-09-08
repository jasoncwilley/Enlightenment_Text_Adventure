from collections import OrderedDict
from player import Player
import world


def play():
    print()
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("Your current adventure come to an end, an end of your choosing.  Not all paths lead to the other side of the City but are they not just as equally important as those that do?  You and only you can determine sucess or failure, each adventure is as unique as the adventurer.  'It is in your moments of decision that your destiny is shaped'.-- Anthony Robbins."  )


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("\r\n""What do you choose to do:?")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("\r\n Actions are the seed of fate; deeds grow into destiny. --Jean Nidetch""\r\n")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Press i to look in Backpack")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Press n to Go North")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Press s to Go South")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Press e to Go East")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Press w to Go West")
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


play()
