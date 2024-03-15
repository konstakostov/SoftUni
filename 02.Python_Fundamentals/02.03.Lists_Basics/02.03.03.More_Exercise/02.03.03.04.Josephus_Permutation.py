people = list(map(int, input().split()))
k = int(input())

victims = []
killed = 0


while len(people) > 0:
    killed = (killed + k) // len(people)
    if killed >= len(people):
        killed -= len(people)

    victims.append(people[abs(killed)])
    people.pop(killed)

# while n > 0:
#         num_in_people = (num_in_people + k) % n
#         removed = people.pop(num_in_people)
#         new.append(removed)
#         n -= 1


print(victims)





# people = input().split()
# k = int(input()) - 1
# n = len(people)
# new = []
# num_in_people = 0
# all_elements = ""
#
# for i in range(1, len(people) + 1):
#     while n > 0:
#         num_in_people = (num_in_people + k) % n
#         removed = people.pop(num_in_people)
#         new.append(removed)
#         n -= 1
#
# new_integers = [int(j) for j in new]
#
# for x in new:
#     new_integers = ','.join(new)
#
# print("[" + new_integers + "]")


# while len(victims_digits) > 0:
#     for victim in victims_digits:
#         counter += 1
#
#         if counter == k:
#             suicide_order.append(victim)
#             victims_digits.remove(victim)
#             counter = 1
#
#
# print(suicide_order)
