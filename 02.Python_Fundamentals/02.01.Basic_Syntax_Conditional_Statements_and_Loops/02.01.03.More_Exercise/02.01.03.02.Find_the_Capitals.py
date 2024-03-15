word = input()

word_list = list(word)

capitals = [c for c in range(len(word_list)) if word_list[c].isupper()]

print(capitals)
