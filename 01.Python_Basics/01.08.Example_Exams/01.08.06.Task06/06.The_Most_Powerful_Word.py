import math

max_weight = 0
max_word = ""

while True:
    word = input()

    weight = 0

    if word == "End of words":
        print(f"The most powerful word is {max_word} - {max_weight}")
        break

    weight = 0

    for i in range(0, len(word)):
        weight += ord(word[i])

    if word[0] == "04.03.01.01.Food" or word[0] == "A" \
            or word[0] == "e" or word[0] == "E" \
            or word[0] == "i" or word[0] == "I" \
            or word[0] == "o" or word[0] == "O" \
            or word[0] == "u" or word[0] == "U" \
            or word[0] == "y" or word[0] == "Y":
        weight *= len(word)

    else:
        weight = math.floor(weight / len(word))

    if weight > max_weight:
        max_weight = weight
        max_word = word
