class Poker:
    def __init__(self):
        self.cards = [
            {"+": "A"}, {"+": "K"}, {"+": "Q"}, {"+": "J"}, {"+": "10-"}, {"+": "9"}, {"+": "8"}, {"+": "7"}, {"+": "6"},
            {"-": "A"}, {"-": "K"}, {"-": "Q"}, {"-": "J"}, {"-": "10-"}, {"-": "9"}, {"-": "8"}, {"-": "7"}, {"-": "6"},
            {"*": "A"}, {"*": "K"}, {"*": "Q"}, {"*": "J"}, {"*": "10-"}, {"*": "9"}, {"*": "8"}, {"*": "7"}, {"*": "6"},
            {"/": "A"}, {"/": "K"}, {"/": "Q"}, {"/": "J"}, {"/": "10-"}, {"/": "9"}, {"/": "8"}, {"/": "7"}, {"/": "6"},
        ]
        self.hand = []
        self.table = []
        self.max_card = 19

    def give_cards(self):
        """Выдает игроку две случайные карты и удаляет их из колоды
        """
        import random
        for i in range(2):
            random_card = int(random.randint(0, self.max_card))
            self.hand.append(self.cards[random_card])
            self.cards.pop(random_card)
            self.max_card -= 1

    def put_cards_on_table(self, count):
        """Выставляет count случайных карт на стол и удаляет их из колоды
        """
        import random
        for i in range(count):
            random_card = int(random.randint(0, self.max_card))
            self.table.append(self.cards[random_card])
            self.cards.pop(random_card)
            self.max_card -= 1
        input("Нажмите Enter, чтобы продолжить...")

    def show_hand(self):
        """Возвращает руку (карты) игрока
        """
        return self.hand

    def show_table(self):
        """Возвращает карты, находящиеся на столе
        """
        return self.table

    def find_combination(self, hand, table):
        """Находит комбинации, исходя из карт на руках и столе. Если комбинаций нет, то возвращает False
        """
        combo = hand + table

        import count
        count1 = count.Count()

        for card in combo: # list -> dict
            suit = list(card.keys())[0]
            value = card[suit]

            count1.add_suit_count(suit)
            count1.add_value_count(value)

        import combinations
        combination = combinations.Combinations(count1.suit_count, count1.value_count)

        return combination.find_combo()