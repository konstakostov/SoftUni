skumria_price = float(input())
caca_price = float(input())

palamud = float(input())
safrid = float(input())
midi = float(input())

palamud_price = skumria_price + skumria_price * 0.60
safrid_price = caca_price + caca_price * 0.80
midi_price = 7.50

palamud_sum = palamud * palamud_price
safrid_sum = safrid * safrid_price
midi_sum = midi * midi_price

total_sum = (palamud_sum + safrid_sum + midi_sum)

print(f"{total_sum:.2f}")
