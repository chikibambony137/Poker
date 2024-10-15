import poker

class Count:
    def __init__(self, deck_cards):
        self.suit_count = {"+": 0, "-": 0, "*": 0, "/": 0}
        self.value_count = {}
        self.value_count = self.init_value_count(self.value_count, deck_cards)

    def count_cards_in_combo(self, combo: list) -> dict:

        for card in combo:

            suit = list(card.keys())[0]
            value = card[suit]

            self.add_suit_count(suit)
            self.add_value_count(value)

        return self.suit_count, self.value_count

    def add_suit_count(self, suit):
        """Увеличивает количество карт одинаковой масти
        """
        self.suit_count[suit] += 1

    def add_value_count(self, value):
        """Увеличивает количество карт одинакового достоинства
        """
        self.value_count[value] += 1

    def init_value_count(self, value_dict: dict, deck: list):
        """Возвращает словарь с количеством карт разного достоинства (0 по умолчанию)
        """
        for card in deck:
            suit = list(card.keys())[0]
            value = card[suit]
            if value not in value_dict:
                value_dict[value] = 0
        return value_dict