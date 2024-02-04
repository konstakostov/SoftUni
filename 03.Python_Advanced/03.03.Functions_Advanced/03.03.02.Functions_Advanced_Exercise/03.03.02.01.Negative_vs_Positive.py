def num_print(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        return print("The positives are stronger than the negatives")
    else:
        return print("The negatives are stronger than the positives")


num_list = [int(x) for x in input().split()]

positive_sum = sum(x for x in num_list if x > 0)
negative_sum = sum(x for x in num_list if x < 0)

num_print(positive_sum, negative_sum)
