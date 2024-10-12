import random
class Poker:
    def __init__(self):
        self.cards = [
            {"+": "A"}, {"+": "K"}, {"+": "Q"}, {"+": "J"}, {"+": "10"},
            {"-": "A"}, {"-": "K"}, {"-": "Q"}, {"-": "J"}, {"-": "10"},
            {"*": "A"}, {"*": "K"}, {"*": "Q"}, {"*": "J"}, {"*": "10"},
            {"/": "A"}, {"/": "K"}, {"/": "Q"}, {"/": "J"}, {"/": "10"},
        ]
        self.hand = []
        self.table = []
        self.max_card = 19

    def give_cards(self):
        for i in range(2):
            random_card = int(random.randint(0, self.max_card))
            self.hand.append(self.cards[random_card])
            self.cards.pop(random_card)
            self.max_card -= 1
        self.show_hand()

    def put_cards_on_table(self, count):
        for i in range(count):
            random_card = int(random.randint(0, self.max_card))
            self.table.append(self.cards[random_card])
            self.cards.pop(random_card)
            self.max_card -= 1
        self.show_table()
        input("Нажмите Enter, чтобы продолжить...")

    def show_hand(self):
        print(f"Ваши карты: {self.hand}")

    def show_table(self):
        print(f"На столе: {self.table}")

    def end(self):
        self.show_hand()
        self.find_combination(self.hand, self.table)

    def find_combination(self, hand, table):
        combo = hand + table

        countChervi = 0
        countVinni = 0
        countKresti = 0
        countBubi = 0

        countA = 0
        countK = 0
        countQ = 0
        countJ = 0
        count10 = 0

        for card in combo:
            for suit in card:
                match suit:
                    case "+":
                        countChervi += 1
                    case "-":
                        countVinni += 1
                    case "*":
                        countKresti += 1
                    case "/":
                        countBubi += 1
            for value in card:
                match card[value]:
                    case "A":
                        countA += 1
                    case "K":
                        countK += 1
                    case "Q":
                        countQ += 1
                    case "J":
                        countJ += 1
                    case "10":
                        count10 += 1

        print(countChervi, countVinni, countKresti, countBubi, "\n",
                countA, countK, countQ, countJ, count10)
        

if __name__ == "__main__":
    poker = Poker()
    poker.give_cards()
    poker.put_cards_on_table(3)
    poker.put_cards_on_table(1)
    poker.put_cards_on_table(1)
    poker.end()
