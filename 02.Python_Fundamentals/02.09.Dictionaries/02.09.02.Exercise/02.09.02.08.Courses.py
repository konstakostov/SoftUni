courses = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

for course_name, student_name in courses.items():
    registered_students = len(courses[course_name])

    print(f"{course_name}: {registered_students}")
    for name in student_name:
        print(f"-- {name}")
