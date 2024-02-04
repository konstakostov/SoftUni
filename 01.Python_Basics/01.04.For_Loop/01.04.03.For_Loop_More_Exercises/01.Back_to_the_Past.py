inheritance = float(input())
final_year = int(input())

age = 18
total_spending = 0

for year in range(1800, final_year + 1):

    if year % 2 == 0:
        total_spending += 12000
        age += 1
    else:
        total_spending += 12000 + (50 * age)
        age += 1

if total_spending > inheritance:
    print(f"He will need {(total_spending - inheritance):.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {(inheritance - total_spending):.2f} dollars left.")
