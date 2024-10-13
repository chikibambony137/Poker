def play():
    import poker
    poker1 = poker.Poker()
    poker1.give_cards()
    print(f"Ваши карты: {poker1.show_hand()}")
    poker1.put_cards_on_table(3)
    print(f"На столе: {poker1.show_table()}")
    poker1.put_cards_on_table(1)
    print(f"На столе: {poker1.show_table()}")
    poker1.put_cards_on_table(1)
    print(f"На столе: {poker1.show_table()}")
    print(f"Ваши карты: {poker1.show_hand()}")

    result = poker1.find_combination(poker1.hand, poker1.table)
    if not result:
        print("Повезет в следующий раз! :D", result)
    else:
        print(f"Поздравляем! У вас {result["Combo"]} {result["Value"]}")
        
if __name__ == "__main__":
    play()