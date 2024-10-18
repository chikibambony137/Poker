import poker, sys
from os import system

def clear_line(count: int):
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    for i in range(count):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def clear_full():
    system("cls")

def hand(poker: poker.Poker):
    print(f"Ваши карты: {poker.show_hand()}")

def table(poker: poker.Poker):
    print(f"На столе: {poker.show_table()}")

def continue_():
    input("Нажмите Enter, чтобы продолжить...")

def lose():
    print("Повезет в следующий раз! :D")

def win(res: dict):
    print(f"Поздравляем! У вас {res["Combo"]} {res["Value"]}")

def result(poker: poker.Poker):
    result = poker.find_combination(poker.hand, poker.table)
    if result == None:
        lose()
    else:
        win(result)