academy = {}

pair_of_rows = int(input())

for i in range(pair_of_rows):
    name = input()
    grade = float(input())

    academy[name] = academy.get(name, {"grade": 0, "num_of_grades": 0})

    academy[name]["grade"] += grade
    academy[name]["num_of_grades"] += 1


for name, grade in academy.items():
    average_grade = grade["grade"] / grade["num_of_grades"]
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
