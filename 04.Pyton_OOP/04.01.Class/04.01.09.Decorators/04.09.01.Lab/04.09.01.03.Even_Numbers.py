def even_numbers(function):
    def wrapper(numbers):
        result = function(numbers)

        even_nums = [e for e in result if e % 2 == 0]

        return even_nums

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
