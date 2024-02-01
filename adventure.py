"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# TODO: MAKE SURE TO WRITE COMPLETE DOCSTRINGS, PRECONDITIONS, AND REPRESENTATION INVARIANTS

# Note: You may add in other import statements here as needed
# from game_data import World, Item, Location, Player
from world import World
from player import Player
from location import Location
from item import Item

# from npc import NPC
# Note: You may add helper functions, classes, etc. here as needed

def parse_input(input: str) -> None:
    """parses the player input and calls the corresponding method in the player
    class based on the key words in the player input. The player methods then further
    check that the choice is valid based on representation invariants of player or 
    available moves

    Preconditions:
    - TODO
    """ 
    command = input.split(' ')
    for i in range(len(command)):
        command[i] = command[i].lower()

    # Handle movement cases
    if command[0] == 'north' or command[0] == 'south' or command[0] == 'west' or command[0] == 'east':
        # print('debug: reach a')
        game_player.move(command[0])
    elif command[0] == 'move':
        if len(command) > 1:
            if command[1] == 'north' or command[1] == 'south' or command[1] == 'west' or command[1] == 'east':
                game_player.move(command[1])
            else:
                print('Cannot move there!')
        else:
            print('move where? \n')



    return


# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    # NOTE: game world and player have been initialized in another file to avoid circular import issue
    # this is because for movement, player needs to know the size of the map but player is imported here too
    # game_world = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    # game_player = Player(3, 4)  # set starting location of player; you may change the x, y coordinates here as appropriate

    # menu = ["look", "inventory", "score", "quit", "back"]
    # location_descriptions = {}

    game_world = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    game_player = Player(4, 3, game_world.map)  # set starting location of player

    while not game_player.victory:
        location = game_world.get_location(game_player.x, game_player.y)

        if location.num_visited == 0:
            print(location.long_desc + '\n')
        else:
            print(location.short_desc + '\n')
        # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)

        player_input = input("What to do? ")
        parse_input(player_input)     # parses player command and decides correct player method
        # TODO
        # while parse_input(player_input) == False:
        #     player_input = input("Invalid command! What to do? ")
        # print("[menu]")

        # for action in location.available_actions():
        #     print(action)
        # choice = input("\nEnter action: ")

        # if choice == "[menu]":
        #     print("Menu Options: \n")
        #     for option in menu:
        #         print(option)
        #     choice = input("\nChoose action: ")

        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
