n = int(input())

sum_01 = 0
sum_02 = 0
sum_03 = 0
sum_04 = 0


for _ in range(1, 2):
    num = int(input())
    sum_01 += num

for _ in range(1, 2):
    num = int(input())
    sum_02 += num

for _ in range(1, 2):
    num = int(input())
    sum_03 += num

for _ in range(1, 2):
    num = int(input())
    sum_04 += num

n = int(input())

diff_01 = 0
diff_02 = 0
diff_03 = 0


if sum_01 == sum_02 == sum_03 == sum_04:
    print(f"Yes, value={sum_01}")

else:
    if sum_01 != sum_02:
        diff_01 = abs(sum_01 - sum_02)
    if sum_02 != sum_03:
        diff_02 = abs(sum_02 - sum_03)
    if sum_03 != sum_04:
        diff_03 = abs(sum_03 - sum_04)

    if diff_01 > diff_02 and diff_01 > diff_03:
        print(f"No, maxdiff={diff_01}")
    elif diff_02 > diff_01 and diff_02 > diff_03:
        print(f"No, maxdiff={diff_02}")
    elif diff_03 > diff_02 and diff_03 > diff_01:
        print(f"No, maxdiff={diff_03}")



