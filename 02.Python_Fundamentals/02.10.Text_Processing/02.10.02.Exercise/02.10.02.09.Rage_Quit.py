initial_message = input()
rage_message = ""

text_to_repeat = ""
repeat_as_string = ""
last_char = ""

for char in initial_message:
    if char.isnumeric():
        repeat_as_string += char

    else:
        if last_char.isnumeric():
            repeat = int(repeat_as_string)
            rage_message += text_to_repeat.upper() * repeat

            text_to_repeat = ""
            repeat_as_string = ""

        text_to_repeat += char

    last_char = char

if last_char.isnumeric():
    repeat = int(repeat_as_string)
    rage_message += text_to_repeat.upper() * repeat

    text_to_repeat = ""
    repeat_as_string = ""

unique_symbols = ''.join(set(rage_message))

print(f"Unique symbols used: {len(unique_symbols)}")
print(rage_message)
