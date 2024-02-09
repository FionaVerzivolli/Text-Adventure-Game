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

class Item:
    """An item in our text adventure game world.
       
        Representation Invariants:
        - self.start_location is not None
        - self.end_location is not None
        - self.name is not None
        - self.name is not ''
        - self.points >= 0
        """
    def __init__(self,start_location: int, end_location: int, points: int, name: str):
        """Method that creates an item object 
        Preconditions:
            - -1 <= start_location <= 11
            - -1 <= end_location <= 11
            - points >= 0
            - name != ''
        """
        self.start_location = start_location 
        self.end_location = end_location
        self.points = points
        self.name = name

    def print_statement(self, used_successfully: bool) -> None:
        raise NotImplementedError

class Key(Item): 
    """A key item in our text adventure game world."""

    def __init__(self, start_location: int, end_location: int, points: int, name: str):
        """Initialize our key 
        Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''
            """
        # initalize our item
        super().__init__(start_location, end_location, points, name)
    

    def print_statement(self, used_successfully: bool) -> None:
        """Determine whether our key has been used successfully"""

        if used_successfully:
            print('You have used key successfully! \n')
            print('You have unlocked the CSSU lounge \n')
        else:
            print('You cannot use the key here! \n')

class T_card(Item):
    """Our T-card item and functionalities. """

    def __init__(self, start_location: int, end_location: int, points: int, name: str):
        """Initialize our T-Card object 
          Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''"""
        super().__init__(start_location, end_location, points, name)
    
    def print_statement(self, used_successfully: bool) -> None:
        if used_successfully:
            print('You have deposited your t-card in successfully! \n')
        else:
            print('You cannot deposited your t-card here! \n')

class Lucky_pen(Item):
    """Our lucky-pen item. """
    def __init__(self, start_location: int, end_location: int, points: int, name: str):
        """ Create our T-Card object.
         Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''"""
        super().__init__(start_location, end_location, points, name)
    
    def print_statement(self, used_successfully: bool) -> None:
        if used_successfully:
            print('You have deposited your lucky pen in successfully! \n')
        else:
            print('You cannot deposited your lucky pen here! \n')

class Cheatsheet(Item):
    """Our Cheatsheet item """
    def __init__(self, start_location: int, end_location: int, points: int, name: str):
        """Create our cheat-sheet object.
          Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''
             """
        super().__init__(start_location, end_location, points, name)
    
    def print_statement(self, used_successfully: bool) -> None:
        if used_successfully:
            print('You have deposited your cheat sheet in successfully! \n')
        else:
            print('You cannot deposited your cheat sheet here! \n')

class IceCreamSandwich(Item):
    """Our icecream sandwich item."""
    def __init__(self, start_location: int, end_location: int, points: int, name: str):
        """Create our icecream-sandwich object.
          Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''
        """
        super().__init__(start_location, end_location, points, name)
    
    def print_statement(self, used_successfully: bool) -> None:
        if used_successfully:
            print('You have given your ice cream successfully! \n')
            print('The suspicious man tells you to SEARCH the rocket in Myhal center for your lucky pen \n')
        else:
            print('You cannot give your ice cream here! \n')

class Flowers(Item):
    """ Our Flowers item"""
    def __init__(self, start_location: int, end_location: int, points: int, name: str):
        """Create our flowers object.
          Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''
        """
        super().__init__(start_location, end_location, points, name)
    
    def print_statement(self, used_successfully: bool) -> None:
        if used_successfully:
            print('You have given your flowers successfully! \n')
            print('Fairgrieve tells you that the answer to Ilias riddle is 42 \n')
        else:
            print('You cannot give your flowers here! \n')



class ItemFactory:
    """ Store all our items and their classes """

    item_classes = {
        'Key': Key,
        'T_card': T_card,
        'Lucky_pen': Lucky_pen,
        'Cheatsheet': Cheatsheet,
        'IceCreamSandwich': IceCreamSandwich,
        'Flowers': Flowers
    }

    
    @staticmethod
    def create_item(start_location: int, end_location: int, points: int, name: str) -> Item:
        """Method that creates an item, similar to the methods of our previous class"""
        # create the item
        item_class = ItemFactory.item_classes.get(name, Item)
        # return our item
        return item_class(start_location, end_location, points, name)




