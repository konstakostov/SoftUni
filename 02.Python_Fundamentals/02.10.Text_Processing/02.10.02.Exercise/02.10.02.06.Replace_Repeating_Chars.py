text = input()
new_text = ""
last_letter = ""

for letter in text:
    if letter != last_letter:
        new_text += letter
        last_letter = letter

print(new_text)
