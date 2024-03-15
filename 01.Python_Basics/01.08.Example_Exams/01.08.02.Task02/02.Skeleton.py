minutes = int(input()) * 60
seconds = int(input())
tunnel = float(input())
hundred_m = int(input())

time_total = minutes + seconds
time_lost = (tunnel / 120) * 2.5

time_needed = ((tunnel / 100) * hundred_m) - time_lost

if time_needed <= time_total:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_needed:.3f}.")
else:
    print(f"No, Marin failed! He was {(time_needed - time_total):.3f} second slower.")
