fat_1gr = 9
protein_1gr = 4
carb_1gr = 4

fat_percent = int(input()) / 100
protein_percent = int(input()) / 100
carbs_percent = int(input()) / 100
calories_total = int(input())
water_percent = int(input()) / 100

fats_gr = (calories_total * fat_percent) / fat_1gr
proteins_gr = (calories_total * protein_percent) / protein_1gr
carbs_gr = (calories_total * carbs_percent) / carb_1gr

gr_total = fats_gr + proteins_gr + carbs_gr

calorie_1gr = calories_total / gr_total

calorie_1gr *= (1 - water_percent)

print(f"{calorie_1gr:.4f}")
