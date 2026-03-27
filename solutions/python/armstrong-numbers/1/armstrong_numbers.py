"""Functions for determining Armstrong numbers.

About Armstrong numbers:
https://en.wikipedia.org/wiki/Narcissistic_number
"""


def is_armstrong_number(number: int) -> bool:
    """Check whether a number is an Armstrong number.

    :param number: the number to test for the Armstrong number property.
    :return: True if the number is an Armstrong number, False otherwise.
    """
    number_in_str = str(number)
    total = 0
    for digit in range(len(number_in_str)):
        total += int(number_in_str[digit]) ** len(number_in_str)
    return total == number
