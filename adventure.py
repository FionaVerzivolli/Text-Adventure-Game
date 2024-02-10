"""Main file that the game should be run from"""

from world import World
from player import Player

# NOTE: all pyta errors have been addressed, except for forbidden imports and print, which
#       are both permitted on ed


def one_word_command(word: str, a_player: Player, a_world: World) -> tuple[Player, World]:
    """
    Helper function for parse input to reduce complexity of main function, 
    deals with one word commands
    """
    # look command
    if word == 'look':
        print(a_world.get_location(a_player.x, a_player.y).long_desc + '\n')

    # code for when the user enters the correct answer for our math problem
    elif word == '42':
        if a_world.map[a_player.y][a_player.x] == 11:
            print('Ilia, impressed by your genius solution wants to give you a cheatsheet! \n')
            cheatsheet_item = a_world.item_dict['Cheatsheet']
            # player earns respective points
            a_player.score += cheatsheet_item.points
            # player gets cheatsheet
            a_player.add_item(cheatsheet_item)

    # inventory command
    elif word == 'inventory':
        a_player.print_inventory()

    # score command
    elif word == 'score':
        print(f'your score is: {a_player.score} \n')

    # quit command, after this all length 1 commands are dealt with
    elif word == 'quit':
        print('thanks for playing! \n')
        quit()
    return a_player, a_world


def pickup_drop(command: list[str], a_player: Player, a_world: World) -> tuple[Player, World]:
    """Helper function for pick up and drop commands. Reduces complexity of main parse function"""
    if command[0] == 'pickup':
        # store the removed item object in a temporary variable
        temp = a_world.remove_item(command[1], a_player.game_map[a_player.y][a_player.x], len(a_player.inventory))
        # if there is no removed item object display error message
        if temp is not None:
            a_player.add_item(temp)

    elif command[0] == 'drop':
        temp = a_player.remove_item(command[1])
        if temp is not None:
            a_world.add_item(command[1], a_world.map[a_player.y][a_player.x])
    return a_player, a_world


def parse_input(input_str: str, a_player: Player, a_world: World) -> tuple[Player, World]:
    """parses the player input and calls the corresponding method in the player
    class based on the key words in the player input. The player methods then further
    check that the choice is valid based on representation invariants of player or
    available moves.

    Preconditions:
    - len(input) > 0
    - all([isalpha(x) for x in input])
    """
    # make our input lowercase to make it easier to check
    input_str = input_str.lower()
    # list of replacement words
    replacement_words = [('move', 'go'), ('pick up', 'pickup'), ('flowers', 'Flowers'),
                         ('ice cream', 'IceCreamSandwich'), ('ice cream sandwich', 'IceCreamSandwich'),
                         ('pen', 'Luckypen'), ('take', 'pickup'), ('lucky pen', 'Luckypen'), ('lucky pen', 'Luckypen'),
                         ('cheatsheet', 'Cheatsheet'), ('cheat sheet', 'Cheatsheet'), ('give', 'use'),
                         ('t card', 'Tcard'), ('t-card', 'Tcard'), ('tcard', 'Tcard'), ('key', 'Key'),
                         ('enter', 'give'), ('cssu lounge', 'lounge')]
    for replacement in replacement_words:
        input_str = input_str.replace(replacement[0], replacement[1])
    # get rid of all spaces
    command = input_str.split(' ')

    # length 0 or special length 1 command, ask again for input
    if len(command) == 0 or (len(command) == 1 and command[0] not in ['inventory', 'quit', 'look', 'score', '42']):
        print(" What??? \n")

    elif command[0] in ['inventory', 'quit', 'look', 'score', '42']:
        a_player, a_world = one_word_command(command[0], a_player, a_world)

    # handle movement cases
    elif command[0] == 'go':
        a_player.move(command[1], a_world.location_dict)

    # pick up, drop, and search for items
    elif command[0] in ['pickup', 'drop']:
        a_player, a_world = pickup_drop(command, a_player, a_world)
    # elif command[0] == 'pickup':
    #     # store the removed item object in a temporary variable
    #     temp = a_world.remove_item(command[1], a_player.game_map[a_player.y][a_player.x], len(a_player.inventory))
    #     # if there is no removed item object display error message
    #     if temp is not None:
    #         a_player.add_item(temp)

    # elif command[0] == 'drop':
    #     temp = a_player.remove_item(command[1])
    #     if temp is not None:
    #         a_world.add_item(command[1], a_world.map[a_player.y][a_player.x])
    # search command
    elif command[0] == 'search':
        # store the searched object in a temporary variable
        temp = a_world.search(a_world.map[a_player.y][a_player.x], command[1], len(a_player.inventory))
        # if the player finds an object, add to inventory and increase score
        if temp is not None:
            a_player.add_item(temp)
            a_player.score += temp.points

    # use command
    elif command[0] == 'use':
        # implemented this way for pyta indentation error
        try:
            # generate a list of names of items in theplayer's inventory
            inventory_names = [item.name for item in a_player.inventory]
            item_index = inventory_names.index(command[1])
            # try using this item on the player's current location
            is_success = a_world.use(command[1], a_world.map[a_player.y][a_player.x])
            # print whether we were able to use our item, using polymorphic method in item.py
            print(a_player.inventory[item_index].print_statement(is_success))   # NOTE: use of polymorphic code here

            # if we were able to use this item, update our score and remove item from inventory
            if is_success:
                removed_item = a_player.inventory.pop(item_index)
                a_player.score += removed_item.points
        except ValueError:
            print('item not in inventory')

    elif command[0] == 'deposit':
        a_player.deposit(command[1], a_world.map[a_player.y][a_player.x])
    else:
        # invalid input case
        print("I do not understand that! \n")

    return a_player, a_world


if __name__ == "__main__":

    # open all of our text files for their information
    with open('map.txt') as map_file, open('locations.txt') as location_file, open('items.txt') as item_file:
        world = World(map_file, location_file, item_file)

    # create our player using the player class
    player = Player(4, 3, world.map)

    print('\n')
    # initialize amount of time left and amount of deposited items
    TIME_LEFT = 90

    # while the player still has time and hasn't deposited all the items, continue the game
    while TIME_LEFT > 0 and player.deposited < 3:
        # update location
        location = world.get_location(player.x, player.y)
        print(f'Location: {player.game_map[player.y][player.x]}')
        # if the player hasn't visited the location
        if not location.visited:
            # print out long description and add points
            print(location.long_desc + '\n')
            player.score += location.num_points
            # update location's visited attribute to be True, indicating the player visited this location
            world.location_dict[world.map[player.y][player.x]].visited = True
        else:
            # if visited attribute is already True, print out short description
            print(location.short_desc + '\n')

        print(f'***** You have {TIME_LEFT} minutes to get to exam! You better hurry, cannot make mistakes! *****\n')

        # give the player a prompt
        player_input = input("What to do? ")
        # parses player command and decides correct player method
        player, world = parse_input(player_input, player, world)
        # after each move, the player's time decreases
        TIME_LEFT -= 1

        # if there is no time left end the game
        if TIME_LEFT == 0:
            print('YOU HAVE RUN OUT OF TIME AND YOU FAIL YOUR EXAM, NO CS POST! \n')
            quit()
        # if the player gets all 3 items they win
        if player.deposited == 3:
            print('YOU HAVE DEPOSITED ALL THE ITEMS AND ENTER THE EXAM SUCCESSFULLY! YOU WIN \n')
            quit()

        # import python_ta

        # python_ta.check_all(config={
        #     'max-line-length': 120,
        # })
