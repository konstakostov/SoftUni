from string import punctuation

with open("text.txt", "r") as input_file:
    text = input_file.readlines()

output_file = open('output.txt', 'w')

for i in range(len(text)):
    letters = 0
    punctuation_mark = 0

    for char in text[i]:
        if char.isalpha():
            letters += 1
        elif char in punctuation:
            punctuation_mark += 1

    output_file.write(f"Line {i + 1}: {''.join(text[i])[:-1]} ({letters})({punctuation_mark})\n")

output_file.close()
