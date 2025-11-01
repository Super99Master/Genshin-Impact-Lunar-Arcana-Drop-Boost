arcana_cards = [
    "Magician",
    "Priestess",
    "Empress",
    "Emperor",
    "Hierophant",
    "Lovers",
    "Chariot",
    "Strength",
    "Heremit",
    "Wheel",
    "Justice",
    "Hanged",
    "Death",
    "Temperance",
    "Devil",
    "Tower",
    "Star",
    "Moon",
    "Sun",
    "Judgment",
    "World",
    "Fool",
]

def is_valid_card(number: int, name: str) -> bool:
    return arcana_cards[number - 1] == name