max_score = 0
max_movie = ""

score = 0
points = 0
movie = ""

for i in range(7):
    movie = input()

    score = 0

    if movie == "STOP":
        print(f"The best movie for you is {max_movie} with {max_score} ASCII sum.")
        raise SystemExit

    for j in range(len(movie)):
        points = ord(movie[j])
        score += points
        if 65 <= points <= 90:
            score -= len(movie)
        elif 97 <= points <= 122:
            score -= len(movie) * 2

    if score > max_score:
        max_score = score
        max_movie = movie

print(f"The limit is reached.")
print(f"The best movie for you is {max_movie} with {max_score} ASCII sum.")
