"""Module with function to determine if year is a leap year or not
"""


def leap_year(year:int) -> bool:
    """Determine if a year is a leap year or not

    :param year: the year that we will determine if it's a leap year.
    :return: return True if year is a leap year, otherwise return False
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
