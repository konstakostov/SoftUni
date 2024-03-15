clock_cycles = [int(x) for x in input().split(', ')]
index = int(input())

total_cycles = 0

while True:
    min_cycle = min(x for x in clock_cycles if x != "")
    min_cycle_index = clock_cycles.index(min_cycle)

    total_cycles += min_cycle

    if min_cycle_index == index:
        break

    clock_cycles[min_cycle_index] = ""

print(total_cycles)
