from config.deck import Deck

class Combinations:
    def __init__(self, suit_count: dict, value_count: dict, table_hand: list, hand: list):

        self.suit_count = suit_count
        self.value_count = value_count
        self.table_hand = table_hand
        self.hand = hand
        self.deck = Deck()

        self.found_combo = {"Combo": "", "Value": None}

        self.fullhouse_value = ""
        self.two_doubles_value = ""
        self.street = []

    def find_combo(self):
        """Ищет комбинации на столе у игрока. Возвращает комбинацию или None, если их нет
        """
        if self.find_kare() == False:
            if self.find_fullhouse() == False:
                if self.find_flash():
                    if self.find_street_flash():
                        self.find_flash_royale()
                elif self.find_street(self.table_hand) == False:
                    if self.find_set() == False:
                        if self.find_double():
                            self.find_two_doubles()
                        else:
                            self.find_high_card()

        return self.found_combo
    
    def find_high_card(self):
        i = 0
        for card in self.hand:
            for suit in card:
                if self.deck.value_priority[card[suit]] > i:
                    high_card = card
                    i = self.deck.value_priority[card[suit]]
        self.found_combo.update(Combo="старшая карта", Value=high_card)
        return True

    def find_double(self) -> bool:
        """Ищет одну пару карт одинакового достоинства. При наличии возвращает True
        """
        for value in self.value_count:
            if self.value_count[value] == 2:
                self.found_combo.update(Combo="пара", Value=value * 2)

                self.two_doubles_value += value * 2

                return True
        return False
    
    def find_two_doubles(self) -> bool:
        """Если найдены две пары, то True, иначе False
        """
        for value in self.value_count:
            if self.value_count[value] == 2 and value not in self.two_doubles_value:
                self.two_doubles_value += value * 2
                self.found_combo.update(Combo="две пары", Value=self.two_doubles_value)

                return True

    def find_set(self) -> bool:
        """Ищет сет (тройку) карт одинакового достоинства. При наличии возвращает True, иначе False
        """
        for value in self.value_count:
            if self.value_count[value] == 3:
                self.found_combo.update(Combo="сет", Value=value * 3)

                self.fullhouse_value += value * 3 + "-"

                return True
        return False
    
    def find_street(self, list) -> bool:
        
        # Преобразуем карты в список достоинств
        values = []
        for card in list:
            for suit in card:
                card_value = card[suit]
            if card_value == 'A':
                values.append(1)  # Туз как единица
                values.append(14)  # Туз как высшая карта
            else:
                values.append(self.deck.value_priority[card_value])
        
        # Удаляем дубликаты и сортируем значения в обратном порядке для поиска старшего стрита
        values = sorted(set(values), reverse=True)

        # Ищем старший стрит
        for i in range(len(values) - 4):
            # Проверяем последовательности из 5 карт
            if values[i] - values[i + 4] == 4:  # Значит, есть последовательность
                # Формируем итоговый список из оригинальных карт
                street = []
                for j in range(5):
                    value = values[i] - j
                    if value == 14 or value == 1:
                        card_value = 'A'
                    else:
                        card_value = next((k for k, v in self.deck.value_priority.items() if v == value), str(value))

                    street.append(card_value)
                    
                self.found_combo.update(Combo="стрит", Value=street)
                self.street = street
                return True

        return False

    def find_flash(self) -> bool:
        for suit in self.suit_count:
            if self.suit_count[suit] >= 5:
                self.flash_suit = suit
                self.flash_list = []
                for card in self.table_hand:
                    for i in card.keys():
                        if i == suit:
                            self.flash_list.append(card)
                sort_flash = sorted(self.flash_list, key=lambda x: x[suit])
                while len(sort_flash) > 5:
                    sort_flash.pop(0)

                self.found_combo.update(Combo="флеш", Value=sort_flash)
                return True
        return False

    def find_fullhouse(self) -> bool:
        """Если найдены сет и пара из различных карт (фуллхаус), то True, иначе False
        """
        if self.find_set():
            for value in self.value_count:
                if self.value_count[value] == 2 and value not in self.fullhouse_value:
                    self.fullhouse_value += value * 2
                    self.found_combo.update(Combo="фулл-хаус", Value=self.fullhouse_value)
                    return True
        return False
                
    def find_kare(self) -> bool:
        """Ищет каре (4 карты) одинакового достоинства. При наличии возвращает True, иначе False.
        """
        for value in self.value_count:
            if self.value_count[value] == 4:
                self.found_combo.update(Combo="каре", Value=value * 4)
                return True
        return False

    def find_street_flash(self) -> bool:
        if self.find_street(self.flash_list) == True:
            self.found_combo.update(Combo='стрит-флеш', Value=[self.street, self.flash_suit])
            return True

    def find_flash_royale(self) -> bool:
        if self.street == ['A', 'K', 'Q', 'J', '10-']:
            self.found_combo.update(Combo='ФЛЕШ-РОЯЯЯЯЯЯЛЬ!', Value=[self.street, self.flash_suit])
            return True
