secret_message = input().split()

decoded_message = []

for word in secret_message:
    num_str = ""
    letters_str = ""

    for symbol in word:
        if symbol.isdigit():
            num_str += symbol
        else:
            letters_str += symbol

    num_as_letter = chr(int(num_str))
    word_as_string = num_as_letter + letters_str

    word_as_list = list(word_as_string)
    word_as_list[1], word_as_list[-1] = word_as_list[-1], word_as_list[1]

    decoded_word = "".join(word_as_list)

    decoded_message.append(decoded_word)

print(" ".join(decoded_message))
