import math

num_people = int(input())
capacity_people = int(input())

courses = math.ceil(num_people / capacity_people)

print(courses)
