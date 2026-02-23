"""Use while loop to cunt instance and get evens."""

__author__ = "730947912"


def num_instances(phrase: str, search_char: str) -> int:
    """Count search character show in phrase."""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count


def get_evens(numbers: str) -> str:
    """Get even for numbers and put them back."""
    evens: str = ""
    index: int = 0
    while index < len(numbers):
        if int(numbers[index]) % 2 == 0:
            evens = evens + numbers[index]
        index = index + 1
    return evens
