movie = input()
days = int(input())
tickets = int(input())
tickets_price = float(input())
cinema_percent = int(input()) / 100

profit = days * (tickets * tickets_price)
profit *= (1 - cinema_percent)

print(f"The profit from the movie {movie} is {profit:.2f} lv.")
