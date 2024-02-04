sq_m = int(input())

one_sq_m_price = 7.61
sq_m_full_price = sq_m * one_sq_m_price

discount = sq_m_full_price * 0.18

sq_m_disc_price = sq_m_full_price - discount

print(f"The final price is: {sq_m_disc_price} lv.")
print(f"The discpunt is: {discount} lv.")
