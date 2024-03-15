# # Variant 01
# people = int(input())
# wagons = input().split()
#
# index = 0
#
# while index <= (len(wagons) - 1):
#     max_people_wagon = 4
#     starting_people = int(wagons[index])
#     final_people = 0
#
#     if starting_people <= max_people_wagon <= people:
#         final_people += max_people_wagon - starting_people
#         people -= final_people
#     else:
#         final_people += people
#         people -= final_people
#
#     wagons[index] = str(int(wagons[index]) + final_people)
#
#     index += 1
#
# if people <= 0:
#     print("The lift has empty spots!")
#     print(" ".join(wagons))
# else:
#     print(f"There isn't enough space! {people} people in 04.03.01.01.Food queue!")
#     print(" ".join(wagons))


# Variant 02
people = int(input())
wagons = [int(x) for x in input().split()]

for i in range(len(wagons)):
    max_people = min(4 - wagons[i], people)
    wagons[i] += max_people
    people -= max_people

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif any(current_wagon < 4 for current_wagon in wagons):
    print("The lift has empty spots!")

print(*wagons, sep=" ")
