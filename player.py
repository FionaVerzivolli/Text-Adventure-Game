"""Module for player class"""

from typing import Optional
from item import Item
from location import Location
import item

# NOTE: most pyta errors have been addressed except module imports and prints, which is permitted


class Player:
    """
    A Player in the text adventure game.

    Instance Attributes:
        - x: integer for x coordinate of player position
        - y: integer for y coordinate of player position
        - game_map: list of list of int representing game map (useful for move method)
        - score: int representing player score
        - inventory: list of items in players inventory
        - max_weight: int representing max inventory size
        - deposited: int representing number of deposited items

    Representation Invariants:
        - 0 <= x < len(self.game_map[0])
        - 0 <= y < len(self.game_map)
        - self.score >= 0
        - self.max_weight == 2
        - self.game_map != [] and self.game_map != [[]]
        - all([len(self.game_map[n]) == len(self.game_map[n + 1]) for n in range(0, len(self.game_map) - 1)])
    """
    x: int
    y: int
    game_map: list[list[int]]
    score: int
    inventory: list[item.Item]
    max_weight: int
    deposited: int

    def __init__(self, x: int, y: int, game_map: list[list[int]]) -> None:
        """
        Initializes a new Player at position (x, y).

        - game_map: 2d list of ints, map
        """
        self.x = x
        self.y = y
        self.game_map = game_map
        self.score = 0
        self.inventory = []
        self.max_weight = 2
        self.deposited = 0

    def north(self, location_dict: dict[int, Location]) -> None:
        """Helper function for north for move method"""
        if self.y - 1 < 0:
            print("You cannot move outside boundaries \n")
            # if movement results in an unreachable area, display the correct message
        elif self.game_map[self.y - 1][self.x] == -1:
            print("You cannot move there \n")
        elif location_dict[self.game_map[self.y - 1][self.x]].locked:
            print('room is locked \n')
        # if there are no issues, proceed and update the correct coordinate
        # same logic applies to every other elif/else branch
        else:
            self.y -= 1

    def south(self, location_dict: dict[int, Location]) -> None:
        """Helper function for south in move method"""
        if self.y + 1 > len(self.game_map) - 1:
            print("You cannot move outside boundaries \n")
        elif self.game_map[self.y + 1][self.x] == -1:
            print("You cannot move there \n")
        elif location_dict[self.game_map[self.y + 1][self.x]].locked:
            print('room is locked \n')
        else:
            self.y += 1

    def west(self, location_dict: dict[int, Location]) -> None:
        """Helper function for west in move method"""
        if self.x - 1 < 0:
            print("You cannot move outside boundaries \n")
        elif self.game_map[self.y][self.x - 1] == -1:
            print("You cannot move there \n")
        elif location_dict[self.game_map[self.y][self.x - 1]].locked:
            print('room is locked \n')
        else:
            self.x -= 1

    def east(self, location_dict: dict[int, Location]) -> None:
        """Helper function for east move method"""
        if self.x + 1 > len(self.game_map[0]) - 1:
            print("You cannot move outside boundaries \n")
        elif self.game_map[self.y][self.x + 1] == -1:
            print("You cannot move there \n")
        elif location_dict[self.game_map[self.y][self.x + 1]].locked:
            print('room is locked \n')
        else:
            self.x += 1

    def move(self, choice: str, location_dict: dict[int, Location]) -> None:
        """
        Our movement function for our player.
        The player can move in 4 directions, North, South, East or West,
        depending on the adjacent rooms.

        Preconditions:
        - choice == 'north' or choice == 'west' or choice == 'south' or choice == 'east'
        - location_dict != {}

        Doctests:
        >>> from world import World
        >>> sample_map_data = open("map.txt")
        >>> sample_location_data = open("locations.txt")
        >>> sample_items_data = open("items.txt")
        >>> sample_world = World(sample_map_data, sample_location_data, sample_items_data)
        >>> sample_dict = sample_world.location_dict

        >>> player = Player(2, 2, [[-1, 11, 9, 10, -1], [-1, -1, 8, -1, -1], [7, 6, 4, 5, -1], [-1, -1, 3, 2, 1]])
        >>> player.move('south', sample_dict)
        >>> player.x
        2
        >>> player.y
        3
        >>> player.move('west', sample_dict)    # this should not change player position since moving to invalid pos
        >>> player.x
        2
        >>> player.y
        3

       Instance Attributes:
        - choice: str
        """
        # movement cases for each direction, add or subtract to coordinates as required
        if choice == 'north':
            self.north(location_dict)
        elif choice == 'south':
            self.south(location_dict)
        elif choice == 'west':
            self.west(location_dict)
        elif choice == 'east':
            self.east(location_dict)
        return None

    def print_inventory(self) -> None:
        """ Print the player's inventory.
        """
        # if the length is 0, the player has no inventory
        if len(self.inventory) == 0:
            print('empty inventory \n')
        else:
            # otherwise, print full inventory
            print('your inventory is: \n')
            for inventory_item in self.inventory:
                print(f"{inventory_item.name}\n")

    def in_inventory(self, item_name: str) -> bool:
        """ A helper function to check whether an item is in the player's inventory.
        If the item is in inventory, return true, otherwise return false
        """
        for inventory_item in self.inventory:
            if inventory_item.name == item_name:
                return True
        return False

    def add_item(self, add_item: Item) -> None:
        """
        A function to add an item to a player's inventory if inventory isn't full

        Preconditions:
          - item.name != ''
          - item.name is not None
        """

        # if there is room in our inventory (the length is less than the max length)
        if len(self.inventory) < self.max_weight:
            # add the item to our inventory
            print(f'added {add_item.name} to inventory \n')
            self.inventory.append(add_item)
          # otherwise, tell the player to remove an item
        else:
            print('inventory is too full! REMOVE item to pick up new item \n')

    def remove_item(self, item_name: str) -> Optional[Item]:
        """A function used to remove an item from our player's inventory.
        Returns removed item so it can be used in our World class."""

        # check each item in our inventory
        for i in range(len(self.inventory)):
            # if the inventory item's name matched our item's name
            if self.inventory[i].name == item_name:
                # successfully remove this item from inventory and return it
                print(f'removed {item_name} from inventory')
                return self.inventory.pop(i)
        # otherwise, return an error message
        print(f'You do not have {item_name} in your inventory')
        return None

    def deposit(self, item_name: str, location_num: int) -> None:
        """
        Deposit items like key, tcard, or lucky pen at exam cent
        """
        if item_name in ['Cheatsheet', 'Tcard', 'Luckypen'] and location_num == 1:
            # game keeps track of how many required items the player brings to exam center
            if self.in_inventory(item_name):
                self.deposited += 1
                deposited_item = self.remove_item(item_name)
                # player earns points
                self.score += deposited_item.points
                print(deposited_item.print_statement(True))     # NOTE: use of polymorphic code from item.py here
        else:
            print('Cannot deposit here \n')



if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
    })
