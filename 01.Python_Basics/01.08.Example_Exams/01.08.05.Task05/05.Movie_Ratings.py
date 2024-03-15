import sys

quantity = int(input())

max_rating = -sys.maxsize
max_movie = ""

min_rating = sys.maxsize
min_movie = ""

rating_sum = 0

for i in range(quantity):
    movie = input()
    rating = float(input())

    rating_sum += rating

    if rating > max_rating:
        max_rating = rating
        max_movie = movie

    if rating < min_rating:
        min_rating = rating
        min_movie = movie

print(f"{max_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {(rating_sum / quantity):.1f}")
