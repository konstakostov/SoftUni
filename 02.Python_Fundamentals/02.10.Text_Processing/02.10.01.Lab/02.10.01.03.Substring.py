sub_string = input()
string = input()

while sub_string in string:
    string = string.replace(sub_string, "")

print(string)
