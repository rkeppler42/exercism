"""Functions for calculating wheat grains on a chessboard.

Based on the wheat and chessboard problem:
https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem
"""


def square(number: int) -> int:
    """Calculate the number of wheat grains on the given chessboard square.

    :param number: number of chessboard square.
    :return: number of wheat grains on the given square.
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int:
    """Calculate the total number of wheat per chessboard.

    :return: total number of wheat per chessboard.
    """
    total_wheat = 0
    for square_of_chessboard in range(1, 65):
        total_wheat += square(square_of_chessboard)
    return total_wheat
