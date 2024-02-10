"""
The location module contains the Location class for the game. The location class contains data
for each location and is used in world.py by location_dict
All the classes leveraged in adventure.py (main file) are kept separate so code is more modular
and easy to test
"""

# NOTE: This file is checked for most pyta errors, the only unavoidable errors are with too many instance attributes


class Location:
    """A location object in our text adventure game world.

      Instance Attributes:
        - location_num: an integer representing the location's number on map.txt
        - num_points: an integer for the points you get for entering a location for the first time
        - short_desc: a string for the short description of the location
        - long_desc: a string for the long description of the location
        - visited: a boolean representing whether or not the location has been visited or not
        - locked: a boolean representing whether or not the location is locked
        - searchable: a boolean representing whether or not the room is still searchable
        - available_items: a list of strings containing items available in the room currently
      
      Representation Invariants:
        - isinstance(self.location_num, int)
        - isinstance(self.num_points, int)
        - len(self.short_desc) > 0 and len(self.long_desc) > 0 and len(self.short_desc) <= len(self.long_desc)
        - self.location_num -1 <= 0 <= 11
        - self.num_points >= 0
        - len(self.short_desc) > 0 and len(self.short_desc) < len(self.long_desc)

    """
    location_num: int
    num_points: int
    short_desc: str
    long_desc: str
    visited: bool
    locked: bool
    searchable: bool
    available_items: list[str]

    def __init__(self, location_num: int, num_points: int, short_desc: str, long_desc: str, visited: bool,
                 locked: bool, searchable: bool, available_items: list[str]) -> None:
        """Initialize a new location.

        NOTE: pyta raises an error for location because location has 8 instance attributes
              when the max allowed is 7, however the 8 instance attributes are necessary.
              location_num, num_points, short_desc, long_desc, locked, and available_items are 
              instance attributes necessary (5 attributes already) for baseline 75% performance.
              locked is necessary to check if a room is open or not, and searchable is necessary
              to check if a room is still searchable for items or not as part of our games
              enhancements
        
        NOTE: pyta raises an error for the arguments of __init__ because a max of 5 instance attributes
              are allowed but 8 are used. However, all 8 of them are variable depending on the location
              and are extracted from the data file location.txt. Thus, they cannot be removed in the 
              initialization. Moreover, 6 of these attributes are for baseline functionality
        NOTE: although arguments themselves could be passed as a separate object to avoid the error, 
              but it adds no value to the code to and instead complicates the code unnecessarily.
              On ed, its mentioned if necessary, extra attributes are fine
        """

        self.location_num = location_num
        self.num_points = num_points
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.visited = visited
        self.locked = locked
        self.searchable = searchable
        self.available_items = available_items


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
    })
