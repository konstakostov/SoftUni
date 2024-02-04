employees = input().split(" ")
improvement_factor = int(input())

employees = list(map(lambda x: int(x) * improvement_factor, employees))

filtered_happiness = list(filter(lambda y: y >= sum(employees) / len(employees), employees))

if len(filtered_happiness) >= len(employees) / 2:
    print(f"Score: {len(filtered_happiness)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_happiness)}/{len(employees)}. Employees are not happy!")
