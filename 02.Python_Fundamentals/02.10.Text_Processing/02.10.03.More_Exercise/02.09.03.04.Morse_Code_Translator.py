morse_code = {'.-': "A", '-...': "B", '-.-.': "C", '-..': "D", '.': "E",
              '..-.': "F", '--.': "G", '....': "H", '..': "I", '.---': "J",
              '-.-': "K", '.-..': "L", '--': "M", '-.': "N", '---': "O",
              '.--.': "P", '--.-': "Q", '.-.': "R", '...': "S", '-': "T",
              '..-': "U", '...-': "V", '.--': "W", '-..-': "X", '-.--': "Y",
              '--..': "Z", '-----': "0", '.----': "1", '..---': "2", '...--': "3",
              '....-': "4", '.....': "5", '-....': "6", '--...': "7", '---..': "8",
              '----.': "9"}

text = input()
words = text.split(" | ")
message = []

for word in words:
    chars = word.split()
    word_translated = ""

    for char in chars:
        if char in morse_code:
            word_translated += morse_code.get(char)

    message.append(word_translated)

print(' '.join(message))
