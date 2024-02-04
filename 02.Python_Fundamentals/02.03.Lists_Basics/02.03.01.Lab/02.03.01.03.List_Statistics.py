n = int(input())

positives_list = []
negatives_list = []

for i in range(n):
    num = int(input())

    if num > 0:
        positives_list.append(num)
    elif num < 0:
        negatives_list.append(num)

print(positives_list)
print(negatives_list)

print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum(negatives_list)}")
