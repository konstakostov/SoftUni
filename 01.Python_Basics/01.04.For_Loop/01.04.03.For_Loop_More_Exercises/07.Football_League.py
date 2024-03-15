capacity = int(input())
fans_amount = int(input())

# People in Different Sectors
sec_a = 0       # Sector A
sec_b = 0       # Sector B
sec_v = 0       # Sector V
sec_g = 0       # Sector G

for _ in range(1, fans_amount + 1):
    fan = input()

    if fan == "A":
        sec_a += 1
    elif fan == "B":
        sec_b += 1
    elif fan == "V":
        sec_v += 1
    elif fan == "G":
        sec_g += 1

# People in Different Sectors - Percentage
sec_a_perc = (sec_a / fans_amount) * 100      # Sector A
sec_b_perc = (sec_b / fans_amount) * 100      # Sector B
sec_v_perc = (sec_v / fans_amount) * 100      # Sector V
sec_g_perc = (sec_g / fans_amount) * 100      # Sector G

# Fans to Stadium Capacity Ratio in Percentage
fans_capacity_ratio = (fans_amount / capacity) * 100

# Printed Results
print(f"{sec_a_perc:.2f}%")
print(f"{sec_b_perc:.2f}%")
print(f"{sec_v_perc:.2f}%")
print(f"{sec_g_perc:.2f}%")
print(f"{fans_capacity_ratio:.2f}%")
