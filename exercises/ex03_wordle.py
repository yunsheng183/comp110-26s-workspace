__author__ = "730947912"

WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def input_guess(secret_word_len: int) -> str:
    """To guess the correct length."""
    guess: str = input(f"Enter a {secret_word_len} character word: ")

    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Guess the character founds in secret word."""
    assert len(char_guess) == 1
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emoji string comparing guess to secret word."""
    assert len(guess) == len(secret)
    result: str = ""
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1
    return result


def main(secret: str) -> None:
    """The entrypoint and main loop."""
    turn: int = 1
    max_turns: int = 6
    while turn <= max_turns:
        print(f"=== Turn {turn}/{max_turns} ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/{max_turns} turns!")
            return
        turn += 1

    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
