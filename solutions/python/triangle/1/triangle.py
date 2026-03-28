"""Functions for determining triangle validity and type.

About triangles:
https://en.wikipedia.org/wiki/Triangle
"""

def equilateral(sides: list) -> bool:

    """Determine if three sides result in an equilateral triangle.

    :param sides: a list consisting of three lengths.
    :return: True if sides result in an equilateral triangle, False otherwise.
    """
    if not is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] and sides[0] == sides[2]


def isosceles(sides: list) -> bool:

    """Determine if three sides result in an isosceles triangle.

    :param sides: a list consisting of three lengths.
    :return: True if sides result in an isosceles triangle, False otherwise
    """
    if not is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides: list) -> bool:
    
    """Determine if three sides result in an scalene triangle.

    :param sides: a list consisting of three lengths.
    :return: True if sides result in a scalene triangle.
    """
    if not is_valid_triangle(sides):
        return False
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]


def is_valid_triangle(sides: list) -> bool:
    """Determine if three sides result in a valid triangle.

    :param sides: a list consisting of three lengths.
    :return: Determine if three sides result in a valid triangle.
    """
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False
    if sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1] or sides[1] + sides[2] < sides[0]:
        return False
    return True
