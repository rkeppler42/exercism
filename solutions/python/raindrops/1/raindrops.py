"""Module that returns a string based on the number divisibility.

If the number is divisible by 3, add "Pling" to the result,
if the number is divisible by 5, add "Plang" to the result,
if the number is divisible by 7, add "Plong" to the result,
if the number is not divisible by 3, 5, and 7, return it as a string.

For more information:
https://exercism.org/tracks/python/exercises/raindrops
"""


def convert(number: int) -> str:
    """Convert a number into a string based on its divisibility.

    :param number: an integer number that will be converted.
    :return: the string based on the number divisibility.
    """
    return_string = ""
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
    if number % 3 == 0:
        return_string += "Pling"
    if number % 5 == 0:
        return_string += "Plang"
    if number % 7 == 0:
        return_string += "Plong"
    return return_string
