nums = list(map(int, input().split()))

average = sum(nums) / len(nums)

greater_average = []

for elem in nums:
    if elem > average:
        greater_average.append(elem)


greater_average.sort(reverse=True)

while len(greater_average) > 5:
    greater_average.remove(greater_average[-1])

if len(greater_average) == 0:
    print("No")
else:
    print(*greater_average, sep=" ")

