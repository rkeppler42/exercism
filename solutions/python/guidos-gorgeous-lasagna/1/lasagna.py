"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_baked_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_baked_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time in minutes

    :param number_of_layers: int - number of layers of the lasagna.
    :return: int - time in minutes that it will take to prepare the lasagna derived from 'number_of_layers' and 'PREPARATION_TIME'.

    Function that takes the number of layers the lasagna will have as
    an argument and returns the preparation time in minutes based on
    the 'PREPARATION_TIME'.
    """
    return number_of_layers * PREPARATION_TIME    


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the time spent in the kitchen between preparation and baking.

    :param number_of_layers: int - number of layers of the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - time spent in the kitchen between preparation and baking.

    Function that takes the the number_of_layers, elapsed_bake_time and return
    the amount of time spent in the kitchen.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time