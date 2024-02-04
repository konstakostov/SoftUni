month = input()
nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = nights * 50
    apartment = nights * 65
    if nights > 14:
        studio *= 0.70
    elif nights > 7:
        studio *= 0.95

elif month == "June" or month == "September":
    studio = nights * 75.20
    apartment = nights * 68.70
    if nights > 14:
        studio *= 0.80

elif month == "July" or month == "August":
    studio = nights * 76
    apartment = nights * 77

if nights > 14:
    apartment *= 0.90

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")


# # HOTEL ROOM
# month = input()
# nights = int(input())
#
# studio = 0
# apartment = 0
#
# if month == "May" or "October":
#     studio = 50
#     apartment = 65
#
#     if nights > 14:
#         studio *= 0.70
#     elif nights > 7:
#         studio *= 0.95
#
# elif month == "June" or "September":
#     studio = 75.20
#     apartment = 68.70
#
#     if nights > 14:
#         studio *= 0.80
#
# else:
#     studio = 76
#     apartment = 77
#
# if nights > 14:
#     apartment *= 0.90
#
# print(f"Apartment: {(nights * apartment):.2f} lv")
# print(f"Studio: {(nights * studio):.2f} lv.")