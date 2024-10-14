import console, poker

def preflop(poker: poker.Poker):
    console.clear_full()
    poker.give_cards()
    console.hand(poker)
    console.continue_()

def flop(poker: poker.Poker):
    console.clear_line(1)
    poker.put_cards_on_table(3)
    console.table(poker)
    console.continue_()

def turn(poker: poker.Poker):
    console.clear_line(2)
    poker.put_cards_on_table(1)
    console.table(poker)
    console.continue_()

def river(poker: poker.Poker):
    console.clear_line(2)
    poker.put_cards_on_table(1)
    console.table(poker)
    console.continue_()

def showdown(poker: poker.Poker):
    console.clear_line(1)
    console.result(poker)