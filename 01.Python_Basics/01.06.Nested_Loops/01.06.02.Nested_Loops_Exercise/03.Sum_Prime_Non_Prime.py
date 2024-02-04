sum_prime = 0
sum_non_prime = 0

while True:
    command = input()

    if command == "stop":
        break

    current_num = int(command)
    is_prime = True

    if current_num < 0:
        print("Number is negative.")
        continue

    for number in range(2, current_num):
        if current_num % number == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += current_num
    else:
        sum_non_prime += current_num

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")

