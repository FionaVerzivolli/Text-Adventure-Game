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

class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - location_num: an integer representing the location's number on map.txt
        - num_points: integer for the points you get for entering a location for the first time
        - short_desc: a string for the short description of the location
        - long_desc: a string for the long description of the location
        - num_visited: an integer representing the number of times this location is visited

    Representation Invariants:
        - self.num_points >= 0
        - len(self.short_desc) > 0
        - len(self.long_desc) > 0
        - self.num_visited >= 0
    """

    def __init__(self, location_num: int, num_points: int, short_desc: str, long_desc: str, num_visited: int) -> None:
        """Initialize a new location.

        # TODO Add preconditions/more details here about the initialization if needed
        """

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

        # TODO: Complete this method
        self.location_num = location_num
        self.num_points = num_points
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.num_visited = num_visited

    def available_actions(self):
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """

        # NOTE: This is just a suggested method
        # i.e. You may remove/modify/rename this as you like, and complete the
        # function header (e.g. add in parameters, complete the type contract) as needed

        # TODO: Complete this method, if you'd like or remove/replace it if you're not using it

