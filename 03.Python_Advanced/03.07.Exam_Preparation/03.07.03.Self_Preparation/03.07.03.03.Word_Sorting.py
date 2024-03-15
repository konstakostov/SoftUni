def words_sorting(*args):
    result = ""
    dictionary = {}

    for arg in args:
        dictionary[arg] = sum(ord(x) for x in arg)

    if sum(dictionary.values()) % 2 == 0:
        dictionary = sorted(dictionary.items(), key=lambda x: x[0])
    else:
        dictionary = sorted(dictionary.items(), key=lambda x: -x[1])

    for key, value in dictionary:
        result += f"{key} - {value}\n"

    return result.strip()


print(words_sorting('escape',
                    'charm',
                    'mythology'
                    ))

print(words_sorting('escape',
                    'charm',
                    'eye'
                    ))

print(words_sorting('cacophony',
                    'accolade',
                    ))
