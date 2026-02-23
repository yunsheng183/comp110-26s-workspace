def find_small_card(cards: str) -> int:
    index: int = 0
    low_card: int = int(cards[0])

    while index < len(cards):
        if int(cards[index]) < low_card:
            low_card = int(cards[index])
        index = index + 1
    return low_card


print(find_small_card(cards="324549493"))
