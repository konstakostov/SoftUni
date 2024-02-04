num_k = int(input())
num_l = int(input())
num_m = int(input())
num_n = int(input())

counter = 0

for num1_1 in range(num_k, 8 + 1):
    if num1_1 % 2 != 0:
        continue
    for num1_2 in range(9, num_l - 1, -1):
        if num1_2 % 2 == 0:
            continue
        for num2_1 in range(num_m, 8 + 1):
            if num2_1 % 2 != 0:
                continue
            for num2_2 in range(9, num_n - 1, -1):
                if num2_2 % 2 == 0:
                    continue

                if str(num1_1) + str(num1_2) != str(num2_1) + str(num2_2):
                    counter += 1
                    print(f"{num1_1}{num1_2} - {num2_1}{num2_2}")
                else:
                    print("Cannot change the same player.")

                if counter >= 6:
                    raise SystemExit
