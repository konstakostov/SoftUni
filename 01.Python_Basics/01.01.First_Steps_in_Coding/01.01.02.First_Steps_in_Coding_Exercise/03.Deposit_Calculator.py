deposit_sum = float(input())
deposit_deadline = int(input())
year_percent = float(input()) / 100

total_sum = deposit_sum + deposit_deadline * ((deposit_sum * year_percent) / 12)

print(total_sum)


