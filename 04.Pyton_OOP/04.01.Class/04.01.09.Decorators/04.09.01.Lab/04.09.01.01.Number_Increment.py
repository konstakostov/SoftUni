def number_increment(nums):

    def increase():
        return [n + 1 for n in nums]

    return increase()


print(number_increment([1, 2, 3]))
