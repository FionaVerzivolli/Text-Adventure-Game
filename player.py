"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# from adventure import game_world

# from initialize import game_player, game_world

# TODO: need inventory command, player class should store all the methods from player input

class Player:
    """
    A Player in the text adventure game.

    Instance Attributes:
        - x: integer for x coordinate of player position
        - y: integer for y coordinate of player position
        - inventory: list of items in players inventory
        - victory: boolean representing if player has won or not
        - TODO

    Representation Invariants:
        - 0 <= x < len(game_world[0])
        - 0 <= y < len(game_world)
        - TODO
    """
    def __init__(self, x: int, y: int, game_map: list[list[int]]) -> None:
        """
        Initializes a new Player at position (x, y).

        - game_map: 2d list of ints, map 
        """
        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.
        self.x = x
        self.y = y
        self.game_map = game_map
        self.inventory = []
        self.victory = False

    def move(self, choice) -> None:
        """
        TODO: fix doctests to make move invalid if you try to move to LOCATION -1
        Function method used to update a player's position based off of the
        player's input

        Preconditions:
        - choice == 'north' or choice == 'west' or choice == 'south' or choice == 'east'

        >>> player = Player(1, 1)
        >>> player.move('south')
        >>> player.x
        1
        >>> player.y
        0

        >>> player2 = Player(0, 1)
        >>> player2.move('south')
        >>> player2.x
        0
        >>> player2.y
        0

        >>> player3 = Player(1, 1)
        >>> player3.move('north')
        >>> player3.x
        1
        >>> player3.y
        2

       Instance Attributes:
        - choice: str
        """
        # Implemented by: Fiona
        if choice == 'north':
          if self.y - 1 < 0:
            print("You cannot move outside boundaries \n")
          elif self.game_map[self.y - 1][self.x] == -1:
              print("You cannot move there \n")
          else:
            self.y -= 1
        elif choice == 'south':
          if self.y + 1 > len(self.game_map) - 1:
            print("You cannot move outside boundaries \n")
          elif self.game_map[self.y + 1][self.x] == -1:
              print("You cannot move there \n")
          else:
            self.y += 1
        elif choice == 'west':
            if self.x - 1 < 0:
              print("You cannot move outside boundaries \n")
            elif self.game_map[self.y][self.x - 1] == -1:
               print("You cannot move there \n")
            else:
              self.x -= 1
        elif choice == 'east':
            if self.x + 1 > len(self.game_map[0]) - 1:
              print("You cannot move outside boundaries \n")
            elif self.game_map[self.y][self.x + 1] == -1:
               print("You cannot move there \n")
            else:
              self.x += 1
        '''
        initial_x = self.x  # keep track of initial x and y
        initial_y = self.y
        keyword_count = 0  # keep track of the number of keywords
        if "north" in case_gone or "n" in case_gone:  # check if a keyword is mentioned
            self.y += 1
            keyword_count += 1
        if "south" in case_gone or "s" in case_gone:
            keyword_count += 1
            self.y -= 1
        if "east" in case_gone or "s" in case_gone:
            keyword_count += 1
            self.x += 1
        if "west" in case_gone or "w" in case_gone:
            keyword_count += 1
            self.x += 1

        if keyword_count == 0:  # loop if there are no keywords
            choice_2 = input("Please enter a valid input.")
            self.text_parsing_movement(choice_2)

        elif keyword_count > 1:  # loop if there is more than one keyword
            choice_2 = input("Please enter an input with only one direction.")
            self.text_parsing_movement(choice_2)
            self.x = initial_x
            self.y = initial_y
        '''