def vowel_filter(function):
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

    def wrapper():
        return [v for v in function() if v.lower() in VOWELS]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
