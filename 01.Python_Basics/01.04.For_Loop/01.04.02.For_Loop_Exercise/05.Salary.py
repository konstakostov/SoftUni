tabs = int(input())
salary = int(input())

for _ in range(1, tabs + 1):
    site = input()

    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50
    else:
        salary += 0

    if salary <= 0:
        print(f"You have lost your salary.")
        break

else:
    print(salary)
