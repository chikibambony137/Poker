from config.deck import Deck

class Combinations:
    def __init__(self, suit_count: dict, value_count: dict, table_hand: list):

        self.suit_count = suit_count
        self.value_count = value_count
        self.table_hand = table_hand
        self.deck = Deck()

        self.copy_value_count = self.value_count

        self.found_combo = {"Combo": "", "Value": None}

        self.fullhouse_value = ""
        self.two_doubles_value = ""
        self.street_list = []

    def find_combo(self):
        """Ищет комбинации на столе у игрока. Возвращает комбинацию или False, если их нет
        """
        if self.find_kare() == False:
            if self.find_fullhouse() == False:
                if self.find_flash():
                    if self.find_street_flash():
                        self.find_flash_royale()
                elif self.find_street() == False:
                    if self.find_set() == False:
                        if self.find_double():
                            self.find_two_doubles()
                        else:
                            self.find_high_card()

        # if self.find_kare() == False:
        #     if self.find_set() == False:
        #         if self.find_double() == False:
        #             return False
        #         else:
        #             self.find_two_doubles()
        #     else:
        #         self.find_fullhouse()
        return self.found_combo
    
    def find_high_card(self):
        pass

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

    def find_set(self) -> bool:
        """Ищет сет (тройку) карт одинакового достоинства. При наличии возвращает True, иначе False
        """
        for value in self.value_count:
            if self.value_count[value] == 3:
                self.found_combo.update(Combo="сет", Value=value * 3)

                self.fullhouse_value += value * 3 + "-"

                return True
        return False
    
    def find_street(self) -> bool:
        count = 0
        for card in self.table_hand:
            self.street_list = []
            if self.street_recursion(card, count, self.street_list) == True:
                return True
        return False
    
    def street_recursion(self, card: dict, count: int, street: list) -> bool:
        next_card_index = self.deck.cards.index(card) + 1
        count += 1
        street.append(card)
        if count == 5:
            self.found_combo.update(Combo="стрит", Value= self.street_list)
            return True
        elif self.deck.cards[next_card_index] in self.table_hand:
            self.street_recursion(self.deck.cards[next_card_index], count, street)
        else: 
            return False

    def find_flash(self) -> bool:
        for suit in self.suit_count:
            if self.suit_count[suit] >= 5:
                self.found_combo.update(Combo="флеш", Value=suit * 5)
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

        # if self.find_double():
        #     self.found_combo.update(Combo="фулл-хаус", Value=self.fullhouse_value)
        #     return True
        # else: return False
                
    def find_kare(self) -> bool:
        """Ищет каре (4 карты) одинакового достоинства. При наличии возвращает True, иначе False.
        """
        for value in self.value_count:
            if self.value_count[value] == 4:
                self.found_combo.update(Combo="каре", Value=value * 4)
                return True
        return False

    def find_street_flash(self) -> bool:
        pass

    def find_flash_royale(self) -> bool:
        pass