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

from typing import Optional, TextIO
from game_data import Location
from game_data import Item

class World:
    """A text adventure game world storing all location, item and map data.
    Instance Attributes:
        - map: a nested list representation of this world's map
        - int_to_location_dict: a dictionary mapping the location number to a location object
        - item_dict: a dictionary mapping the item name string to the item object
        - # TODO add more instance attributes as needed;

    Representation Invariants:
        - # TODO
    """

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """
        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below

        self.map = self.load_map(map_data)
        self.location_dict = self.load_locations(location_data)
        self.item_dict = self.load_items

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        # Implemented by: Naoroj
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:
        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].
        Return this list representation of the map.

        >>> sample_map_data = open("map.txt")
        >>> sample_location_data = open("locations.txt")
        >>> sample_items_data = open("items.txt")
        >>> sample_world = World(sample_map_data, sample_location_data, sample_items_data)
        >>> sample_world.map == [[-1, 11, 9, 10, -1], [-1, -1, 8, -1, -1], [7, 6, 4, 5, -1], [-1, -1, 3, 2, 1]]
        True
        >>> sample_map_data.close()
        >>> sample_location_data.close()
        >>> sample_items_data.close()
        """

        map_list = []
        for line in map_data:
            row = list(map(int, line.split()))  # this line converts string of integers into list of ints
            # print(row)
            map_list.append(row)
        return map_list

    def load_locations(self, location_data: TextIO) -> dict[int, Location]:
        """
        given a file containing location data, return a dictionary mapping the location number in map.txt
        to the corresponding Location class.

        the method goes on the assumption that a line is the location + num, points, short desc (multiple lines),
        long desc (multiple lines), and END

        >>> sample_map_data = open("map.txt")
        >>> sample_location_data = open("locations.txt")
        >>> sample_items_data = open("items.txt")
        >>> sample_world = World(sample_map_data, sample_location_data, sample_items_data)
        >>> sample_check = sample_world.location_dict
        >>> sample_check[-1].short_desc.strip()
        'That way is blocked.'
        >>> sample_check[10].num_visited
        0
        >>> sample_check[9].long_desc.strip()
        'You are at the end of Saint George Street, to your west is McLennan Physical laboratories and to your right is Myhal Centre.'
        >>> sample_map_data.close()
        >>> sample_location_data.close()
        >>> sample_items_data.close()
        """
        # NOTE: when you change the value of points in locations.txt or whatever else, ensure that
        # the doctests match, be very careful about locations.txt file structure
        location_dict = {}
        line = location_data.readline()  # this reads in junk data to start
        while line.strip() != 'COMPLETE_END':       # loop runs while there are more locations to read  
            new_location = Location(0, 0, '', '', 0)
            line = location_data.readline()
            assert 'LOCATION' in line               
            line = line.split()
            new_location.location_num = int(line[1])    # location number
            line = location_data.readline()
            assert 'NUM_POINTS' in line
            line = line.split()
            new_location.num_points = int(line[1])  # points for entering location
            line = location_data.readline()
            assert line.strip() == '-SHORT'  # here begins sequence of lines for short description
            line = location_data.readline()
            short_desc, long_desc = '', ''
            while line.strip() != '-LONG':      # while sequence for long desc is not reached, add to short desc
                short_desc += line.strip() + ' '
                line = location_data.readline()
            new_location.short_desc = short_desc.strip()
            assert line.strip() == '-LONG'
            line = location_data.readline()
            while line.strip() != 'END':
                long_desc += line.strip() + ' '
                line = location_data.readline()
            new_location.long_desc = long_desc.strip()
            assert line.strip() == 'END'
            line = location_data.readline()
            location_dict[new_location.location_num] = new_location
        return location_dict

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
         Preconditions:
         - 0 <= x < len(self.map[0])
         - 0 <= y < len(self.map)

        >>> sample_map = open("map.txt")
        >>> sample_location = open("locations.txt")
        >>> sample_items = open("items.txt")
        >>> world = World(sample_map, sample_location, sample_items)
        >>> world.get_location(1, 1) is None
        True
        >>> world.get_location(1, 2) == world.location_dict[6]
        True
        """
        game_map = self.map
        locations = self.location_dict
        map_location = game_map[y][x]
        if map_location != -1:
            return locations[map_location]
        return None
