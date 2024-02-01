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

class Player:
    """
    A Player in the text adventure game.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """
    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """
        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.
        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False

    def text_parsing_movement(self, choice) -> None:
        """
        Function method used to update a player's position based off of the
        player's input

        >>> player = Player(1, 1)
        >>> player.text_parsing_movement('move south')
        >>> player.x
        1
        >>> player.y
        0

        >>> player2 = Player(0, 1)
        >>> player2.text_parsing_movement('s outh')
        >>> player2.x
        0
        >>> player2.y
        0

        >>> player3 = Player(1, 1)
        >>> player3.text_parsing_movement('anorth')
        >>> player3.x
        1
        >>> player3.y
        2

       Instance Attributes:
        - choice: str
        """
        # Implemented by: Fiona
        initial_x = self.x  # keep track of initial x and y
        initial_y = self.y
        case_gone = choice.lower()
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
