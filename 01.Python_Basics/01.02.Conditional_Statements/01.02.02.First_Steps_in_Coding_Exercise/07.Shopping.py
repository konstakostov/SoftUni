budget = float(input())

graphic_cards = int(input())
processors = int(input())
ram = int(input())

graphic_cards_price = graphic_cards * 250
processors_price = processors * (graphic_cards_price * 0.35)
ram_price = ram * (graphic_cards_price * 0.10)

final_price = graphic_cards_price + processors_price + ram_price

if graphic_cards > processors:
    final_price *= 0.85

if budget >= final_price:
    print(f"You have {(budget - final_price):.2f} leva left!")
else:
    print(f"Not enough money! You need {(final_price - budget):.2f} leva more!")
