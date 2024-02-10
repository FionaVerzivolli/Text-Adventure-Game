from world import World
from player import Player

def parse_input(input: str) -> None:
    """parses the player input and calls the corresponding method in the player
    class based on the key words in the player input. The player methods then further
    check that the choice is valid based on representation invariants of player or
    available moves.

    Preconditions:
    - len(input) > 0
    - all([isalpha(x) for x in input])
    """
    # make our input lowercase to make it easier to check
    input = input.lower()
    # list of replacement words
    replacement_words = [ ('move', 'go'), ('pick up', 'pickup'), ('flowers', 'Flowers'), ('ice cream', 'IceCreamSandwich'),
                         ('ice cream sandwich', 'IceCreamSandwich'), ('pen', 'Luckypen'), ('take', 'pickup'), ('lucky pen', 'Luckypen'),
                         ('lucky pen', 'Luckypen'), ('cheatsheet', 'Cheatsheet'), ('cheat sheet', 'Cheatsheet'), ('give', 'use'),
                         ('t card', 'Tcard'), ('t-card', 'Tcard'), ('tcard', 'Tcard'), ('key', 'Key'), ('enter', 'give'), ('cssu lounge', 'lounge')]
    for replacement in replacement_words:
        input = input.replace(replacement[0], replacement[1])
    # get rid of all spaces
    command = input.split(' ')

    # error cases
    if len(command) == 0 or (len(command) == 1 and command[0] not in ['inventory', 'quit', 'look', 'score', 'help', '42']):
        print(" What??? \n")
    # handle movement cases
    elif command[0] == 'go':
        if command[1] == 'north' or command[1] == 'south' or command[1] == 'west' or command[1] == 'east':
            game_player.move(command[1], game_world.location_dict)

    # look command
    elif command[0] == 'look':
        print(game_world.get_location(game_player.x, game_player.y).long_desc + '\n')

    # inventory command
    elif command[0] == 'inventory':
        game_player.print_inventory()
    # score command
    elif command[0] == 'score':
        print(f'your score is: {game_player.score + TIME_LEFT} \n')
    # quit command
    elif command[0] == 'quit':
        print('thanks for playing! \n')
        quit()

    # pick up, drop, and search for items
    elif command[0] == 'pickup':
        # store the removed item object in a temporary variable
        temp = game_world.remove_item(command[1], game_player.game_map[game_player.y][game_player.x], len(game_player.inventory))
        # if there is no removed item object display error message
        if temp is None:
            print(f'cannot pick up {command[1]}, it does not exist or inventory is full. You can carry one item max')
        # otherwise, add the item to our player's inventory
        else:
            game_player.add_item(temp)
    elif command[0] == 'drop':
        temp = game_player.remove_item(command[1])
        if temp is not None:
            game_world.add_item(command[1], game_world.map[game_player.y][game_player.x])
    # search command
    elif command[0] == 'search':
        # store the searched object in a temporary variable
        temp = game_world.search(game_world.map[game_player.y][game_player.x], command[1])
        # if the player finds an object, add to inventory and increase score
        if temp is not None:
            print(f'found {temp.name}!')
            game_player.add_item(temp)
            game_player.score += temp.points
        else:
            print('Cannot search that.')

    # use command
    elif command[0] == 'use':
        # implemented this way for pyta indentation error
        try:
            # generate a list of names of items in theplayer's inventory
            inventory_names = [item.name for item in game_player.inventory]
            item_index = inventory_names.index(command[1])
            # try using this item on the player's current location
            is_success = game_world.use(command[1], game_world.map[game_player.y][game_player.x])
            # print whether we were able to use our item, using polymorphic method in item.py
            print(game_player.inventory[item_index].print_statement(is_success))            #NOTE: use of polymorphic code here

            # if we were able to use this item, update our score and remove item from inventory
            if is_success:
                removed_item = game_player.inventory.pop(item_index)
                game_player.score += removed_item.points
        except IndexError:
            print('item not in inventory')

    # code for when the user enters the correct answer for our math problem
    elif command[0] == '42':
        if game_world.map[game_player.y][game_player.x] == 11:
            print('Ilia, impressed by your genius solution gives you a cheatsheet! \n')
            cheatsheet_item = game_world.item_dict['Cheatsheet']
            # player earns respective points
            game_player.score += cheatsheet_item.points
            # player gets cheatsheet
            game_player.add_item(cheatsheet_item)

    elif command[0] == 'deposit':
        if command[1] in ['Key', 'Tcard', 'Luckypen'] and game_world.map[game_player.y][game_player.x] == 1:
            # game keeps track of how many required items the player brings to exam center
            game_player.deposited += 1
            deposited_item = game_player.remove_item(command[1])
            # player earns points
            game_player.score += deposited_item.points
            print(deposited_item.print_statement(True))     # NOTE: use of polymorphic code from item.py here

    else:
        # invalid input case
        print("I do not understand that! \n")

    return None

if __name__ == "__main__":

    # open all of our text files for their information
    with open('map.txt') as map_file, open('locations.txt') as location_file, open('items.txt') as item_file:
        game_world = World(map_file, location_file, item_file)

    # create our player using the player class
    game_player = Player(4, 3, game_world.map)

    print('\n')
    # initialize amount of time left and amount of deposited items
    TIME_LEFT = 120
    deposited_count = 0

    # while the player still has time and hasn't deposited all the items, continue the game
    while TIME_LEFT > 0 and game_player.deposited < 3:
        # update location
        location = game_world.get_location(game_player.x, game_player.y)
        print(f'Location: {game_player.game_map[game_player.y][game_player.x]}')
        # if the player hasn't visited the location
        if not location.visited:
            # print out long description and add points
            print(location.long_desc + '\n')
            game_player.score += location.num_points
            # update location's visited attribute to be True, indicating the player visited this location
            game_world.location_dict[game_world.map[game_player.y][game_player.x]].visited = True
        else:
            # if visited attribute is already True, print out short description
            print(location.short_desc + '\n')

        print(f'***** You have {TIME_LEFT} minutes to get to exam! You better hurry, cannot make mistakes! *****\n')

        # give the player a prompt
        player_input = input("What to do? ")
        # parses player command and decides correct player method
        parse_input(player_input)
        # after each move, the player's time decreases
        TIME_LEFT -= 1
        #if there is no time left end the game
        if TIME_LEFT == 0:
            print('YOU HAVE RUN OUT OF TIME AND YOU FAIL YOUR EXAM, NO CS POST! \n')
            quit()
        # if the player gets all 3 items they win
        if game_player.deposited == 3:
            print('YOU HAVE DEPOSITED ALL THE ITEMS AND WIN! \n')
            quit()

        import python_ta

        python_ta.check_all(config={
            'max-line-length': 120,
        })
