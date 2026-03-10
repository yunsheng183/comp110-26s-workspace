__author__ = "730947912"


def all(input: list[int], value: int) -> bool:
    """Return if all elements true."""
    if len(input) == 0:
        return False
    index: int = 0
    while index < len(input):
        if input[index] != value:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """Return the maximum value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    maximum: int = input[0]
    index: int = 1
    while index < len(input):
        if input[index] > maximum:
            maximum = input[index]
        index += 1
    return maximum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Return True if both lists are equal."""
    if len(list1) != len(list2):
        return False

    index: int = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutate list1 by appending elements of list2."""
    index: int = 0
    while index < len(list2):
        list1.append(list2[index])
        index += 1
