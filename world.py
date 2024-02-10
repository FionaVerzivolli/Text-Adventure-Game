"""This module contains the world class used in adventure."""

from typing import Optional, TextIO
from location import Location
import item

class World:
    """A text adventure game world storing all location, item and map .
    Instance Attributes:
        - map: a nested list representation of this world's map
        - int_to_location_dict: a dictionary mapping the location number to a location object
        - item_dict: a dictionary mapping the item name string to the item object
        - 

    Representation Invariants:
        - map != [[]] or map!= []
        - int_to_location != {}
        - all([len(int_to_location[x]) == 1 for x in range(len(int_to_location)])
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
        self.item_dict = self.load_items(items_data)


        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    def load_map(self, map_data: TextIO) -> list[list[int]]:
        # Implemented by: Naoroj
        # NOTE: The method below is REQUIRED. Complete it exactly as specified.
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
        >>> sample_check[10].visited
        False
        >>> sample_check[9].long_desc.strip()
        'You are at the end of Saint George Street, to your west is McLennan Physical laboratories and to your right is Myhal Centre.'
        >>> sample_check[8].available_items
        ['Flowers']
        >>> sample_map_data.close()
        >>> sample_location_data.close()
        >>> sample_items_data.close()
        """
        # initialize an empty dict
        location_dict = {}
        # reads in junk data to start
        line = location_data.readline() 
        # loop runs while there are more locations to read
        
        while line.strip() != 'COMPLETE_END':      

            new_location = Location(0, 0, '', '', False, False, False, [])
            line = location_data.readline()

            assert 'LOCATION' in line
            line = line.split()
            # location number
            new_location.location_num = int(line[1])  
            line = location_data.readline()

            assert 'NUM_POINTS' in line
            line = line.split()
            # points for entering location
            new_location.num_points = int(line[1])
            line = location_data.readline()

            # here begins sequence of lines for short description
            assert line.strip() == '-SHORT'  
            line = location_data.readline()
            short_desc, long_desc = '', ''

            # while sequence for long desc is not reached, add to short desc
            while line.strip() != '-LONG':    
                short_desc += line.strip() + ' '
                line = location_data.readline()
            new_location.short_desc = short_desc.strip()

            assert line.strip() == '-LONG'
            line = location_data.readline()

            while line.strip() != 'locked' and line.strip() != 'unlocked':
                long_desc += line.strip() + ' '
                line = location_data.readline()
            new_location.long_desc = long_desc.strip()

            assert line.strip() == 'locked' or line.strip() == 'unlocked'
            if line.strip() == 'locked':
                new_location.locked = True
            else:
                new_location.locked = False

            line = location_data.readline()
            assert line.strip() == 'searchable' or line.strip() == 'unsearchable'
            
            if line.strip() == 'searchable':
                new_location.searchable = True
            else:
                new_location.searchable = False

            available_items = []
            line = location_data.readline()

            assert line.strip() == '-AVAILABLE_ITEMS'
            line = location_data.readline()
            while line.strip() != 'END':
                available_items.append(line.strip())
                line = location_data.readline()

            new_location.available_items = available_items

            assert line.strip() == 'END'
            line = location_data.readline()
            location_dict[new_location.location_num] = new_location
        return location_dict


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
        >>> print(world.location_dict)
        >>> world.get_location(1, 2) == world.location_dict[6]
        True
        """

        locations = self.location_dict
        map_location = self.map[y][x]
        if map_location != -1:
            return locations[map_location]
        return None

    def load_items(self, item_data: TextIO) -> dict[str, item.Item]:
        """
        Loading in items using item factory in item.py

        >>> sample_map = open("map.txt")
        >>> sample_location = open("locations.txt")
        >>> sample_items = open("items.txt")
        >>> world = World(sample_map, sample_location, sample_items)
        >>> sample_check = world.load_items(sample_items)
        >>> sample_check['Key'].start_location == 4
        True
        """
        # create empty dict
        item_dict = {}
        line = item_data.readline()

        # continue reading line until the end
        while line.strip() != 'END':
            
            # split the line by spaces
            line = line.split(' ')
            # start location of item
            start_location = int(line[0])
            # end location of item
            end_location = int(line[1])
            # item points
            points = int(line[2])
            # item name
            item_name = line[3].strip()
            # create an item using our data and add it to our dictionary
            item_dict[item_name] = item.ItemFactory.create_item(start_location, end_location, points, item_name)
            # read next line
            line = item_data.readline()
        
        return item_dict

    def remove_item(self, item_name: str, location_number: int, inventory_size: int) -> Optional[item.Item]:
        """remove an item from our location's available items"""

        # check if our item is part of our location's available items
        if item_name in self.location_dict[location_number].available_items and inventory_size < 1: 
            # remove item from our location
            self.location_dict[location_number].available_items.remove(item_name)
            # return item's name
            return self.item_dict[item_name]
        else:
            return None


    def add_item(self, item_name: str, location_number: int) -> None:
        """add an item to our location's available items"""
        self.location_dict[location_number].available_items.append(item_name) 

    def search(self, location_number: int, search_area: str) -> Optional[item.Item]:
        """Search a specific location to find our required items"""

        if location_number == 4:
            # check to see if we searched garbage and our location is searchable
            if search_area == 'garbage' and self.location_dict[location_number].searchable:
                print('Found key! \n')
                # update our location to no longer be searchable
                self.location_dict[location_number].searchable = False
                # return our key item
                return self.item_dict['Key']
            # otherwise, you cannot search the room
            else:
                print('You cannot search that! \n')
                return None
        # same logic but for our other searchable location
        elif location_number == 10:
            if search_area == 'rocket' and self.location_dict[location_number].searchable:
                print('found lucky pen! \n')
                self.location_dict[location_number].searchable = False
                return self.item_dict['Lucky_pen']
            else:
                print('You cannot search that! \n')
                return None
        else:
            print('Cannot search anything here \n')
            return None
    
    def use(self, item_name: str, location_number: int) -> bool:
        """A method that is used to use an object in a location """

        # check specific items 
        if item_name == 'Key':
            # if this item is used in location 6, the door becomes unlocked 
            if location_number == 6:    
                self.location_dict[7].locked = False
                return True
            else:
                return False
        # other items follow the same logic
        elif item_name == 'Flowers':
            if location_number == 5:
                return True
            else:
                return False
        elif item_name == 'IceCreamSandwich':
            if location_number == 3:
                return True
            else:
                return False
        else:
            return False
            
if __name__ == "__main__":
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
    })