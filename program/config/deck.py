class Deck:
    def __init__(self):
        self.cards = [
            {'+': '2'}, {'+': '3'}, {'+': '4'}, {'+': '5'},
            {'+': '6'}, {'+': '7'}, {'+': '8'}, {'+': '9'},
            {'+': '10-'}, {'+': 'J'}, {'+': 'Q'}, {'+': 'K'}, {'+': 'A'},

            {'-': '2'}, {'-': '3'}, {'-': '4'}, {'-': '5'},
            {'-': '6'}, {'-': '7'}, {'-': '8'}, {'-': '9'},
            {'-': '10-'}, {'-': 'J'}, {'-': 'Q'}, {'-': 'K'}, {'-': 'A'}, 
             
            {'*': '2'}, {'*': '3'}, {'*': '4'}, {'*': '5'},
            {'*': '6'}, {'*': '7'}, {'*': '8'}, {'*': '9'},
            {'*': '10-'}, {'*': 'J'}, {'*': 'Q'}, {'*': 'K'}, {'*': 'A'},  
             
            {'/': '2'}, {'/': '3'}, {'/': '4'}, {'/': '5'},
            {'/': '6'}, {'/': '7'}, {'/': '8'}, {'/': '9'},
            {'/': '10-'}, {'/': 'J'}, {'/': 'Q'}, {'/': 'K'}, {'/': 'A'}
        ]
        self.value_priority = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10-': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}