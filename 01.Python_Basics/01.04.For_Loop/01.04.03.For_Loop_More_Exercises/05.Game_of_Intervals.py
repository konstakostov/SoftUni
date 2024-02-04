# Number of Rounds in the Game
rounds = int(input())

# Number Types Occurrences
num_type_1 = 0      # From 0 to 9
num_type_2 = 0      # From 10 to 19
num_type_3 = 0      # From 20 to 29
num_type_4 = 0      # From 30 to 39
num_type_5 = 0      # From 40 to 50
num_type_6 = 0      # Invalid numbers

# Total Points
total_points = 0

# Logic
for _ in range(1, rounds + 1):
    number = int(input())           # Number Given for Each Round

    if 0 <= number <= 9:             # From 0 to 9
        total_points += number * 0.20
        num_type_1 += 1
    elif 10 <= number <= 19:         # From 10 to 19
        total_points += number * 0.30
        num_type_2 += 1
    elif 20 <= number <= 29:         # From 20 to 29
        total_points += number * 0.40
        num_type_3 += 1
    elif 30 <= number <= 39:         # From 30 to 39
        total_points += 50
        num_type_4 += 1
    elif 40 <= number <= 50:         # From 40 to 50
        total_points += 100
        num_type_5 += 1
    else:                           # Invalid numbers
        total_points /= 2
        num_type_6 += 1

# Printed Results

print(f"{total_points:.2f}")
print(f"From 0 to 9: {((num_type_1 / rounds) * 100):.2f}%")
print(f"From 10 to 19: {((num_type_2 / rounds) * 100):.2f}%")
print(f"From 20 to 29: {((num_type_3 / rounds) * 100):.2f}%")
print(f"From 30 to 39: {((num_type_4 / rounds) * 100):.2f}%")
print(f"From 40 to 50: {((num_type_5 / rounds) * 100):.2f}%")
print(f"Invalid numbers: {((num_type_6 / rounds) * 100):.2f}%")
