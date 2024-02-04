def positive(some_num):
    result = [pos for pos in some_num if int(pos) >= 0]
    return result


def negative(some_num):
    result = [neg for neg in some_num if int(neg) < 0]
    return result


def even_nums(some_num):
    result = [even for even in some_num if int(even) % 2 == 0]
    return result


def odd_nums(some_num):
    result = [odd for odd in some_num if int(odd) % 2 != 0]
    return result


input_nums = input().split(", ")

print(f"Positive: {', '.join(positive(input_nums))}")
print(f"Negative: {', '.join(negative(input_nums))}")
print(f"Even: {', '.join(even_nums(input_nums))}")
print(f"Odd: {', '.join(odd_nums(input_nums))}")
