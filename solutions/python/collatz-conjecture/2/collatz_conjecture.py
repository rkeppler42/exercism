"""Functions for calculating steps in the Collatz Conjecture sequence.

About the Collatz Conjecture:
https://en.wikipedia.org/wiki/Collatz_conjecture
"""


def steps(number: int) -> int:
    """Calculate the number of steps to reach 1 following the Collatz Conjecture.

    :param number: positive integer to start the Collatz sequence from.
    :return: number of steps it takes to reach 1 following the Collatz Conjecture.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    while number != 1:
        count += 1
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
    return count
         