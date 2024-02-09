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

from item import Item

class Location:
    """A location object in our text adventure game world.

    Instance Attributes:
        - location_num: an integer representing the location's number on map.txt
        - num_points: integer for the points you get for entering a location for the first time
        - short_desc: a string for the short description of the location
        - long_desc: a string for the long description of the location
        - num_visited: an integer representing the number of times this location is visited


    """

    def __init__(self, location_num: int, num_points: int, short_desc: str, long_desc: str, visited: bool, locked: bool, searchable: bool, available_items: list[str]) -> None:
        """Initialize a new location.

        Representation Invariants:
            - self.num_points >= 0
            - len(self.short_desc) > 0 and len(self.short_desc) < len(self.long_desc)
            - self.num_visited >= 0
            - self.location_num -1 <= 0 <= 11
        """

        self.location_num = location_num
        self.num_points = num_points
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.visited = visited
        self.locked = locked
        self.searchable = searchable
        self.available_items = available_items