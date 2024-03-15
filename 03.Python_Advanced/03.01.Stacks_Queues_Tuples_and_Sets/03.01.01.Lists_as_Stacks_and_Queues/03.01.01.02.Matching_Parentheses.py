text = list(input())

parentheses = []

for index in range(len(text)):
    if text[index] == "(":
        parentheses.append(index)

    if text[index] == ")":
        start = parentheses.pop()
        end = index + 1

        print(*text[start:end], sep="")
