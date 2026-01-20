"""A program to help plan a cozy tea party by calculating supplies and costs"""

__Yunsheng__: str = "730947912"


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed based on the number of people"""
    return people * 3


def treats(people: int) -> int:
    """Calculate the number of treats needed based on the numberof people"""
    return int(tea_bags(people) * 2)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of tea bags and treats."""
    return tea_count * 10 + treat_count * 5


def main_planner(guests: int) -> None:
    """The entrypoint of the program that tea party planning."""

    print("A tea party for " + str(guests) + " people")
    print("Tea Bag:" + (str(tea_bags(people=guests))))
    print("Treats:" + str(treats(people=guests)))
    print(
        "Total Cost:"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending the tea party?")))
