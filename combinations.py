class Combinations:

    def __init__(self, suit_count: dict, value_count: dict):
        self.suit_count = suit_count
        self.value_count = value_count

        self.found_combo = {"Combo": "", "Value": ""}
        self.fullhouse_combo = {"Combo": "", "Value": ""}

    def find_combo(self):
        """Ищет комбинации на столе у игрока. Возвращает комбинацию или False, если их нет
        """
        if self.find_kare() == False:
            if self.find_set() == False:
                if self.find_double() == False:
                    return False
            else:
                self.find_fullhouse()
        return self.found_combo

    def find_double(self) -> bool:
        """Ищет одну пару карт одинакового достоинства. При наличии возвращает True
        """
        for value in self.value_count:
            if self.value_count[value] == 2:
                self.found_combo["Combo"] = "пара"
                self.found_combo["Value"] = value

                self.fullhouse_combo["Value"] += value * 2
                return True
        return False

    def find_set(self) -> bool:
        """Ищет сет (тройку) карт одинакового достоинства. При наличии возвращает True, иначе False
        """
        for value in self.value_count:
            if self.value_count[value] == 3:
                self.found_combo["Combo"] = "сет"
                self.found_combo["Value"] = value

                self.fullhouse_combo["Value"] += value * 3 + "-"
                self.value_count.pop(value)
                return True
        return False
                
    def find_kare(self) -> bool:
        """Ищет каре (4 карты) одинакового достоинства. При наличии возвращает True, иначе False.
        """
        for value in self.value_count:
            if self.value_count[value] == 4:
                self.found_combo["Combo"] = "каре"
                self.found_combo["Value"] = value
                return True
        return False

    def find_fullhouse(self) -> bool:
        """Если найдены сет и пара из различных карт (фуллхаус), то True, иначе False
        """
        if self.find_double():
            self.found_combo.update(Combo="Фулл-хаус", Value=self.fullhouse_combo["Value"])