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
    """An item in our text adventure game world."""
    def use(self) -> None:
        raise NotImplementedError

class Tcard:
    pass

class LuckyPen:
    pass

class Cheatsheet:
    pass

class Bahen_key:
    pass

class IceCreamSandwich:
    pass

class Flowers:
    pass 

"""
    Instance Attributes:
        - name: a string representing the item's name
        - start: an integer representing the item's starting location
        - end: an integer representing where the item should be stored for credit
        - target_points: an 

    Representation Invariants:
        - len(self.name) > 0
        - self.start != -1
        - self.end != -1
        - target_points > 0

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
Initialize a new item.


        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points


"""