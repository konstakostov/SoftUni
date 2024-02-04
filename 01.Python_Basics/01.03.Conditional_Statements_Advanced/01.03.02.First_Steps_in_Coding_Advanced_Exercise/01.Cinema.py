movie_type = input()
rows = int(input())
cols = int(input())

income = 0
seats = rows * cols

if movie_type == "Premiere":
    income = seats * 12

elif movie_type == "Normal":
    income = seats * 7.50

elif movie_type == "Discount":
    income = seats * 5

print(f"{income:.2f} leva")

