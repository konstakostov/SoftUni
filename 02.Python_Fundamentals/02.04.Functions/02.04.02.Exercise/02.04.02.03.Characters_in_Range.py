def characters(char_1, char_2):
    ascii_value_list = []
    ascii_value_string = " "

    char_1_ascii = ord(char_1)
    char_2_ascii = ord(char_2)

    for char_value in range(char_1_ascii + 1, char_2_ascii):
        ascii_value_list.append(chr(char_value))

    return ascii_value_string.join(ascii_value_list)


char_1_input = input()
char_2_input = input()

result = characters(char_1_input, char_2_input)


print(result, end=" ")
