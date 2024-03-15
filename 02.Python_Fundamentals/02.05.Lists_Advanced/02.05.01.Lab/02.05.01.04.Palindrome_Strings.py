input_text = input().split(" ")
given_palindrome = input()

palindromes = []

for word in input_text:
    if word == word[::-1]:
        palindromes.append(word)

given_palindrome_occurrences = palindromes.count(given_palindrome)

print(palindromes)
print(f"Found palindrome {given_palindrome_occurrences} times")
