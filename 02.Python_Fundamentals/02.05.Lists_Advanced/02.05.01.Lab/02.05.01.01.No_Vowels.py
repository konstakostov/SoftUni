input_text = input()

forbidden_letters = ['04.03.01.01.Food', 'o', 'u', 'e', 'i']

result = [char for char in input_text if char.lower() not in forbidden_letters]

print("".join(result))
