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
# TODO: MAKE SURE TO WRITE COMPLETE DOCSTRINGS, PRECONDITIONS, AND REPRESENTATION INVARIANTS

from typing import Optional, TextIO


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - location_num: an integer representing the location's number on map.txt
        - num_points: integer for the points you get for entering a location for the first time
        - short_desc: a string for the short description of the location
        - long_desc: a string for the long description of the location
        - num_visited: an integer representing the number of times this location is visited
        - player_choices: a list of strings representing possible player choices
        - items: a list of strings representing the items in the location


    Representation Invariants:
        - # TODO
    """

    def __init__(self, location_num: int, num_points: int, short_desc: str, long_desc: str, num_visited: int) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
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
        # self.player_choices = player_choices
        # self.items = items

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


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        """Initialize a new item.
        """

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

       e Attributes:
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


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - # TODO add more instance attributes as needed; do NOT remove the map attribute

    Representation Invariants:
        - # TODO
    """

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below

        self.map = self.load_map(map_data)
        self.int_to_location_dict = self.load_locations(location_data)

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
        # TODO: when you change the value of points in locations.txt or whatever else, ensure that
        # the doctests match
        # be very careful about locations.txt file structure,
        # Done by: Naoroj
        """
        given a file containing location data, return a dictionary mapping the location number in map.txt
        to the corresponding Location class.

        the method goes on the assumption that a line is the location + num, points, short desc (multiple lines),
        long desc (multiple lines), and END

        >>> sample_map_data = open("map.txt")
        >>> sample_location_data = open("locations.txt")
        >>> sample_items_data = open("items.txt")
        >>> sample_world = World(sample_map_data, sample_location_data, sample_items_data)
        >>> sample_check = sample_world.int_to_location_dict
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

        int_to_location_dict = {}
        line = location_data.readline()  # this reads in junk data to start

        while line.strip() != 'COMPLETE_END':
            new_location = Location(0, 0, '', '', 0)

            line = location_data.readline()
            assert 'LOCATION' in line
            line = line.split()
            new_location.location_num = int(line[1])
            line = location_data.readline()

            assert 'NUM_POINTS' in line
            line = line.split()
            new_location.num_points = int(line[1])
            line = location_data.readline()

            assert line.strip() == '-SHORT'  # sequence of lines for short and long sec
            line = location_data.readline()
            short_desc, long_desc = '', ''

            while line.strip() != '-LONG':
                short_desc += line.strip() + ' '
                line = location_data.readline()

            new_location.short_desc = short_desc.strip()

            assert line.strip() == '-LONG'
            line = location_data.readline()
            while line.strip() != 'END':
                long_desc += line.strip() + ' '
                line = location_data.readline()
                # print(line + ' 1234')
            new_location.long_desc = long_desc.strip()

            assert line.strip() == 'END'
            line = location_data.readline()
            int_to_location_dict[new_location.location_num] = new_location
        return int_to_location_dict

    # TODO: Add methods for loading item data (see note above).

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
        >>> world.get_location(1, 2) == world.int_to_location_dict[6]
        True

        """

        game_map = self.map
        # print(map)
        locations = self.int_to_location_dict

        map_location = game_map[y][x]
        if map_location != -1:
            return locations[map_location]
        return None
