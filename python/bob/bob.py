"""Module to determine what Bob will reply to someone.

For more information:
https://exercism.org/tracks/python/exercises/bob
"""


def response(hey_bob: str) -> str:
    """Determine Bob's response based on the given input.

    :param hey_bob: a sentence uttered at Bob.
    :return: Bob's response as a string based on the input.
    """
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob[-1] == "?":
        return "Sure."
    return "Whatever."
