num_seq = list(map(int, input().split(", ")))

current_group = []

top_boundary = 10
bottom_boundary = 0

while True:
    for num in num_seq:
        if bottom_boundary < int(num) <= top_boundary:
            current_group.append(num)
    print(f"Group of {top_boundary}'s: {current_group}")

    if top_boundary >= max(num_seq):
        break

    top_boundary += 10
    bottom_boundary += 10
    current_group = []

