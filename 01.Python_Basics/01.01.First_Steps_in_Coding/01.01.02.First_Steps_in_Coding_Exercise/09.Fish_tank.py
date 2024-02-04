length = int(input()) / 10
width = int(input()) / 10
height = int(input()) / 10
percentage = float(input()) / 100

volume_total = length * width * height
volume_occupied = volume_total * percentage

volume_for_water = volume_total - volume_occupied

print(volume_for_water)
