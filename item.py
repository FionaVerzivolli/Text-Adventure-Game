"""
A module containing the item class leveraged by adventure.py.

Item class is an abstract class, which describes the methods our concrete
classes must implement. Concrete classes like Key, T_card, Lucky_pen, etc are
related by ** inheritance ** as part of the ** enhancements **.

NOTE: we are doing an additional feature that uses inheritance in a reasonable way

We used inheritance here as part of a larger feature that allows the player to
use items to solve puzzles by typing 'use [item name]'. The item class has an abstract
method called print_statement which for each item, prints a custom message to the player using
polymorphism.

For items like Key, Tcard, or Luckypen, print_statement simply tells the player whether
or not the item has been used successfully. However, for items like Flowers or IceCreamSandwich,
when used correctly, the player is rewarded with a hint like 'answer 42 to Ilias puzzle' and can
advance successfully in the game

Classes are kept separate in order to keep files modular and easy to test
"""
# NOTE: This file is checked for all pyta errors


class Item:
    """An item in our text adventure game world.

        Representation Invariants:
        - isinstance(self.start_location, int)
        - isinstance(self.end_location, int)
        - len(self.name) > 0
        - self.points >= 0
        """
    start_location: int
    end_location: int
    points: int
    name: str

    def __init__(self, start_location: int, end_location: int, points: int, name: str) -> None:
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

    def print_statement(self, used_successfully: bool) -> str:
        """
        Abstract method that returns custom message depending on whether or
        not an item has been used successfully
        """
        raise NotImplementedError


class Key(Item):
    """A key item in our text adventure game world."""
    start_location: int
    end_location: int
    points: int
    name: str

    def __init__(self, start_location: int, end_location: int, points: int, name: str) -> None:
        """Initialize our key
        Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''
            """
        # initalize our item
        super().__init__(start_location, end_location, points, name)

    def print_statement(self, used_successfully: bool) -> str:
        """
        print whether our key has been used successfully
        >>> key = Key(0, 1, 3, 'test')
        >>> key.print_statement(True)
        'You have used key successfully! \nYou have unlocked the CSSU lounge \n'
        >>> key.print_statement(False)
        'You cannot use the key here! \n'
        """

        if used_successfully:
            return 'You have used key successfully! \nYou have unlocked the CSSU lounge \n'
        else:
            return 'You cannot use the key here! \n'


class Tcard(Item):
    """Our T-card item and functionalities. """
    start_location: int
    end_location: int
    points: int
    name: str

    def __init__(self, start_location: int, end_location: int, points: int, name: str) -> None:
        """Initialize our T-Card object
          Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''"""
        super().__init__(start_location, end_location, points, name)

    def print_statement(self, used_successfully: bool) -> str:
        """
        """
        if used_successfully:
            return 'You have deposited your t-card in successfully! \n'
        else:
            return 'You cannot deposited your t-card here! \n'


class Luckypen(Item):
    """Our lucky-pen item. """
    start_location: int
    end_location: int
    points: int
    name: str

    def __init__(self, start_location: int, end_location: int, points: int, name: str) -> None:
        """ Create our T-Card object.
         Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''"""
        super().__init__(start_location, end_location, points, name)

    def print_statement(self, used_successfully: bool) -> str:
        if used_successfully:
            return 'You have deposited your lucky pen in successfully! \n'
        else:
            return 'You cannot deposited your lucky pen here! \n'


class Cheatsheet(Item):
    """Our Cheatsheet item """
    start_location: int
    end_location: int
    points: int
    name: str

    def __init__(self, start_location: int, end_location: int, points: int, name: str) -> None:
        """Create our cheat-sheet object.
          Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''
             """
        super().__init__(start_location, end_location, points, name)

    def print_statement(self, used_successfully: bool) -> str:
        if used_successfully:
            return 'You have deposited your cheat sheet in successfully! \n'
        else:
            return 'You cannot deposited your cheat sheet here! \n'


class IceCreamSandwich(Item):
    """Our icecream sandwich item."""
    start_location: int
    end_location: int
    points: int
    name: str

    def __init__(self, start_location: int, end_location: int, points: int, name: str) -> str:
        """Create our icecream-sandwich object.
          Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''
        """
        super().__init__(start_location, end_location, points, name)

    def print_statement(self, used_successfully: bool) -> str:
        if used_successfully:
            return 'You have given your ice cream successfully! \nThe suspicious man tells you to SEARCH the rocket\
             in Myhal center for your lucky pen \n'
        else:
            return 'You cannot give your ice cream here! \n'


class Flowers(Item):
    """ Our Flowers item"""
    start_location: int
    end_location: int
    points: int
    name: str

    def __init__(self, start_location: int, end_location: int, points: int, name: str) -> None:
        """Create our flowers object.
          Preconditions:
            - -1 <= start_location <= 11
            - -1 <= start_location <= 11
            - points >= 0
            - name != ''
        """
        super().__init__(start_location, end_location, points, name)

    def print_statement(self, used_successfully: bool) -> str:
        if used_successfully:
            return 'You have given your flowers successfully! \nFairgrieve tells you that the answer to Ilias riddle \
             is 42 \n'
        else:
            return 'You cannot give your flowers here! \n'


class ItemFactory:
    """ Store all our items and their classes """
    item_classes: dict[int, Item]

    item_classes = {
        'Key': Key,
        'Tcard': Tcard,
        'Luckypen': Luckypen,
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


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
    })
