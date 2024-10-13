def play():
    import poker
    poker1 = poker.Poker()
    console_clear_full()

    poker1.give_cards()
    print(f"Ваши карты: {poker1.show_hand()}")
    poker1.put_cards_on_table(3)
    console_clear_line(1)

    print(f"На столе: {poker1.show_table()}")
    poker1.put_cards_on_table(1)
    console_clear_line(2)

    print(f"На столе: {poker1.show_table()}")
    poker1.put_cards_on_table(1)
    console_clear_line(2)

    print(f"На столе: {poker1.show_table()}")

    result = poker1.find_combination(poker1.hand, poker1.table)
    if not result:
        print("Повезет в следующий раз! :D", result)
    else:
        print(f"Поздравляем! У вас {result["Combo"]} {result["Value"]}")

def console_clear_line(count: int):
    import sys
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    for i in range(count):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def console_clear_full():
    from os import system
    system("cls")

if __name__ == "__main__":
    play()