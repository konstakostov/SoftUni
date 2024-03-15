chrysanthemum = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

chrysanthemum_price = 0
roses_price = 0
tulips_price = 0

# Seasonal Pricing
if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2 * chrysanthemum
    roses_price = 4.10 * roses
    tulips_price = 2.50 * tulips

elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75 * chrysanthemum
    roses_price = 4.50 * roses
    tulips_price = 4.15 * tulips

# Holiday Pricing
if holiday == "Y":
    chrysanthemum_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15

# Discounts

flowers_total = chrysanthemum + roses + tulips
bouquet = chrysanthemum_price + roses_price + tulips_price

if season == "Spring" and tulips > 7:
    bouquet *= 0.95
elif season == "Winter" and roses > 10:
    bouquet *= 0.90

if flowers_total > 20:
    bouquet *= 0.80

# Final Price Bouquet + Arrangement 2 leva

bouquet += 2

print(f"{bouquet:.2f}")




# # Seasonal Pricing
# if season == "Spring" or season == "Summer":
#     if holiday == "N":
#         chrysanthemum_price = 2 * chrysanthemum
#         roses_price = 4.10 * roses
#         tulips_price = 2.50 * tulips
#         bouquet = chrysanthemum_price + roses_price + tulips_price
#     elif holiday == "Y":
#         chrysanthemum_price = (2 * chrysanthemum) * 1.15
#         roses_price = (4.10 * roses) * 1.15
#         tulips_price = (2.50 * tulips) * 1.15
#         bouquet = chrysanthemum_price + roses_price + tulips_price
#
# elif season == "Autumn" or season == "Winter":
#     if holiday == "N":
#         chrysanthemum_price = 3.75 * chrysanthemum
#         roses_price = 4.50 * roses
#         tulips_price = 4.15 * tulips
#         bouquet = chrysanthemum_price + roses_price + tulips_price
#     elif holiday == "Y":
#         chrysanthemum_price = (3.75 * chrysanthemum) * 1.15
#         roses_price = (4.50 * roses) * 1.15
#         tulips_price = (4.15 * tulips) * 1.15
#         bouquet = chrysanthemum_price + roses_price + tulips_price
