char_01 = ord(input())
char_02 = ord(input())
text = input()

sum_chars = 0

for char in text:
    if char_01 < ord(char) < char_02:
        sum_chars += ord(char)

print(sum_chars)
