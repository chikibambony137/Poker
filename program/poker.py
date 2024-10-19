class Poker:
    def __init__(self):
        import config.deck as deck, config.count as count
        
        self.deck = deck.Deck()
        self.hand = []
        self.table = []
        self.max_card = len(self.deck.cards) - 1
        self.count1 = count.Count(self.deck.cards)

    def give_cards(self):
        """Выдает игроку две случайные карты и удаляет их из колоды
        """
        import random
        for i in range(2):
            random_card = int(random.randint(0, self.max_card))
            self.hand.append(self.deck.cards[random_card])
            self.deck.cards.pop(random_card)
            self.max_card -= 1

    def put_cards_on_table(self, count):
        """Выставляет count случайных карт на стол и удаляет их из колоды
        """
        import random
        for i in range(count):
            random_card = int(random.randint(0, self.max_card))
            self.table.append(self.deck.cards[random_card])
            self.deck.cards.pop(random_card)
            self.max_card -= 1

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
        table_hand = table + hand

        suit_count, value_count = self.count1.count_cards_in_combo(table_hand)

        import config.combinations as combinations
        combination = combinations.Combinations(suit_count, value_count, table_hand, hand)

        return combination.find_combo()