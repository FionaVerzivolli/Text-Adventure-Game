from typing import Optional, TextIO
from item import Item
from location import Location
from item import IceCreamSandwich


class Player:
    """
    A Player in the text adventure game.

    Instance Attributes:
        - x: integer for x coordinate of player position
        - y: integer for y coordinate of player position
        - inventory: list of items in players inventory
        - game_map: a list of list of ints representing the map for the move method

    Representation Invariants:
        - 0 <= x < len(game_world[0])
        - 0 <= y < len(game_world)
        - TODO
    """
    def __init__(self, x: int, y: int, game_map: list[list[int]]) -> None:
        """
        Initializes a new Player at position (x, y).

        - game_map: 2d list of ints, map 

        Representation Invariants:
          - game_map != [] and game_map != [[]]
          - all([len(game_map[n]) == len(game_map[n + 1]) for n in range(0, len(game_map) - 1)])
          - 0 <= y <= len(game_map)
          - 0 <= x <= len(game_map[0])
        """
        self.x = x
        self.y = y
        self.game_map = game_map
        self.score = 0
        self.inventory = []  
        self.max_weight = 1
        self.deposited = 0

    def move(self, choice: str, location_dict: dict[int, Location]) -> None:
        """
        Our movement function for our player. 
        The player can move in 4 directions, North, South, East or West,
        depending on the adjacent rooms.

        Preconditions:
        - choice == 'north' or choice == 'west' or choice == 'south' or choice == 'east'
        - location_dict != {}

        >>> player = Player(1, 1)
        >>> player.move('south')
        >>> player.x
        1
        >>> player.y
        0

        >>> player2 = Player(0, 1)
        >>> player2.move('south')
        >>> player2.x
        0
        >>> player2.y
        0

        >>> player3 = Player(1, 1)
        >>> player3.move('north')
        >>> player3.x
        1
        >>> player3.y
        2

       Instance Attributes:
        - choice: str
        """
        # movement cases for each direction, add or subtract to coordinates as required
        if choice == 'north':
          # check if movement is within bounds
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
        elif choice == 'south':
          if self.y + 1 > len(self.game_map) - 1:
            print("You cannot move outside boundaries \n")
          elif self.game_map[self.y + 1][self.x] == -1:
              print("You cannot move there \n")
          elif location_dict[self.game_map[self.y + 1][self.x]].locked:
             print('room is locked \n')
          else:
            self.y += 1
        elif choice == 'west':
            if self.x - 1 < 0:
              print("You cannot move outside boundaries \n")
            elif self.game_map[self.y][self.x - 1] == -1:
               print("You cannot move there \n")
            elif location_dict[self.game_map[self.y][self.x - 1]].locked:
             print('room is locked \n')
            else:
              self.x -= 1
        elif choice == 'east':
          if self.x + 1 > len(self.game_map[0]) - 1:
            print("You cannot move outside boundaries \n")
          elif self.game_map[self.y][self.x + 1] == -1:
            print("You cannot move there \n")
          elif location_dict[self.game_map[self.y][self.x + 1]].locked:
            print('room is locked \n')
          else:
            self.x += 1

    def print_inventory(self) -> None:
      """ Print the player's inventory.
      """
      # if the length is 0, the player has no inventory
      if len(self.inventory) == 0:
          print('empty inventory \n')
      else:
        # otherwise, print full inventory
        print('your inventory is: \n')
        for item in self.inventory:
          print(f"{item.name}\n")

    def in_inventory(self, item_name: str) -> bool:
      """ A function to check whether an item is in the player's inventory.
      """
      for item in self.inventory:
        if item.name == item_name:
          return True
      return False

    def add_item(self, item: Item) -> None:
      """
      A function to add an item to a player's inventory.

      Preconditons:
        - item.name != ''
        - item.name is not None
      """

      # if there is room in our inventory (the length is less than the max length)
      if len(self.inventory) < self.max_weight:
        # add the item to our inventory
        print(f'added {item.name} to inventory \n')
        self.inventory.append(item)
      # otherwise, tell the player to remove an item
      else:
        print(f'inventory is too full! REMOVE item to pick up new item \n')

    def remove_item(self, item_name:str) -> Optional[Item]:
        """A function used to remove an item from our player's inventory. 
        Returns removed item so it can be used in our World class."""

        # check each item in our inventory
        for i in range(len(self.inventory)):
          # if the inventory item's name matched our item's name, 
          if self.inventory[i].name == item_name:
            # successfully remove this item from inventory and return it
            print(f'removed {item_name} from inventory')
            return self.inventory.pop(i)
        # otherwise, return an error message
        print(f'You do not have {item_name} in your inventory')
        return None

      
