"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: baking time already elapsed.
    :return: remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time in minutes based on the number of layers of the lasagna.
        
    :param number_of_layers: number of layers of the lasagna.
    :return: time of preparation of the lasagna based on the number of layers and PREPARATION_TIME.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the elapsed time of baking.
    
    :param number_of_layers: number of layers of the lasagna.
    :param elapsed_bake_time: minutes that the lasagna has been cooked for.
    :return: time the lasagna is being prepared and cooked.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


