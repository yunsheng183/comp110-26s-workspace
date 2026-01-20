"""A program to help plan a cozy tea party by calculating supplies and costs"""

__author__: str = "730947912"


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed based on the number of people"""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats needed based on the numberof people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of tea bags and treats."""
    return tea_count * 0.5 + treat_count * 0.75


def main_planner(guests: int) -> None:
    """The entrypoint of the program that tea party planning."""

    print("A cozy tea party for " + str(guests) + " people!")
    print("Tea Bags: " + (str(tea_bags(people=guests))))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending the tea party?")))
