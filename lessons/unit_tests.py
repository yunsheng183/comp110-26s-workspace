def get_first(input_list: list[str]) -> str:
    """Get the first elem."""
    return input_list[0]


def remove_first(input_list: list[str]) -> None:
    """Remove the first elem."""
    input_list.pop(0)


def get_and_remove_first(input_list: list[str]) -> str:
    """Get and remove the first elem."""
    temp: str = get_first(input)
    input_list.pop(0)
    return temp
