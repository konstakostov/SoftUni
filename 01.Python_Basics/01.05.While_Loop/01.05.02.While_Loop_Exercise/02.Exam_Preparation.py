bad_grades_max = int(input())

bad_grades_count = 0
grades_sum = 0
problems_num = 0
last_problem = None

while bad_grades_count < bad_grades_max:
    problem = input()

    if problem == "Enough":
        print(f"Average score: {(grades_sum / problems_num):.2f}")
        print(f"Number of problems: {problems_num}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        bad_grades_count += 1

    grades_sum += grade
    problems_num += 1
    last_problem = problem

else:
    print(f"You need a break, {bad_grades_count} poor grades.")
