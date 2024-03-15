budget = int(input())

spent = 0

while spent <= budget:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        exit()

    spent += int(command)

print("You went in overdraft!")
