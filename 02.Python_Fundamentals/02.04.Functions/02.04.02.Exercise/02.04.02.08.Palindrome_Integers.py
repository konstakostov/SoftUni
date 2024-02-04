def is_palindrome(digit):
    return digit == digit[::-1]


numbers = input().split(", ")

for num in numbers:
    print(is_palindrome(num))
