input_list = input().split()

final_list = [item for item in input_list if len(item) % 2 == 0]

print("\n".join(final_list))
