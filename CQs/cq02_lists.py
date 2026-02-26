"""Mutating functions."""

__author__ = "730947912"


def manual_append(a: list[int], value: int) -> None:
    """Append the value to the list."""
    a.append(value)


def double(a: list[int]) -> None:
    """Double each value in the list."""
    index: int = 0
    while index < len(a):
        a[index] = a[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
