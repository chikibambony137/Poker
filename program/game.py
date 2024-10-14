import poker, config.phases as phases

def play():
    poker1 = poker.Poker()
    phases.preflop(poker1)
    phases.flop(poker1)
    phases.turn(poker1)
    phases.river(poker1)
    phases.showdown(poker1)
