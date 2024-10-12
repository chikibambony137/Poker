class Count:
    def __init__(self):
        self.suit_count = {"+": 0, "-": 0, "*": 0, "/": 0}
        self.value_count = {"A": 0, "K": 0, "Q": 0, "J": 0, "10": 0}

    def add_suit_count(self, suit):
        """Увеличивает количество карт одинаковой масти
        """
        self.suit_count[suit] += 1

    def add_value_count(self, value):
        """Увеличивает количество карт одинакового достоинства
        """
        self.value_count[value] += 1