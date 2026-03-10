__author__ = "730947912"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert input dictionary."""
    result: dict[str, str] = {}
    for key in input_dict:
        value = input_dict[key]
        if value in result:
            raise KeyError("Duplicate key when inverting")
        result[value] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Take input and return the frequency of colors."""
    color_count: dict[str, int] = {}
    for name in colors:
        color = colors[name]

        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    most_color: str = ""
    most_count: int = 0

    for color in color_count:
        if color_count[color] > most_count:
            most_count = color_count[color]
            most_color = color
    return most_color


def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Alphabetizer words."""
    result: dict[str, list[str]] = {}
    for word in words:
        if word[0].isalpha():
            letter = word[0].lower()
            if letter in result:
                result[letter].append(word)
            else:
                result[letter] = [word]
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
