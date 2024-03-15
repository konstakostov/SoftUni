def vowel_filter(function):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    def wrapper():
        return [v for v in function() if v.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "E"]


print(get_letters())
